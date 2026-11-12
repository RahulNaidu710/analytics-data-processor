"""Run only against the disposable services in compose.yaml."""

import json
import subprocess
import uuid

import clickhouse_connect
from redis import Redis
from rq import Queue


def process_sample(datasource_id):
    from domain.common.models import IntegrationProvider
    from event_processors.mixpanel_event_processor import MixPanelEventProcessor
    from store.events_saver import EventsSaver

    records = [
        {"event": "ExampleOpen", "properties": {
            "distinct_id": "example-user-001", "time": 1700000000, "page": "home"}},
        {"event": "ExampleClick", "properties": {
            "distinct_id": "example-user-002", "time": 1700000001, "page": "details"}},
    ]
    dataframe = MixPanelEventProcessor().process(
        "\n".join(json.dumps(record) for record in records)
    )
    saver = EventsSaver()
    try:
        saver.save(datasource_id, IntegrationProvider.MIXPANEL, dataframe)
    finally:
        saver.clickhouse.close()
    return len(dataframe)


def main():
    client = clickhouse_connect.get_client(
        host="clickhouse", allow_experimental_object_type=1
    )
    redis = Redis(host="redis")
    try:
        client.command("""
            CREATE TABLE IF NOT EXISTS events (
                datasource_id String, timestamp DateTime, provider String,
                user_id String, event_name String, properties JSON
            ) ENGINE = MergeTree ORDER BY timestamp
        """)
        datasource_id = "example-" + uuid.uuid4().hex
        job = Queue("platform_default", connection=redis).enqueue(
            "scripts.local_smoke.process_sample", datasource_id, job_timeout=60
        )
        subprocess.run(
            ["rq", "worker", "platform_default", "-c", "settings", "--burst"],
            check=True, timeout=90,
        )
        job.refresh()
        assert job.get_status() == "finished", job.get_status()
        assert job.result == 2, job.result
        rows = client.query(
            "SELECT user_id, event_name, provider, toJSONString(properties) FROM events "
            f"WHERE datasource_id = '{datasource_id}' ORDER BY timestamp"
        ).result_set
        rows = [tuple(row[:3]) + (json.loads(row[3])["properties.page"],) for row in rows]
        assert rows == [
            ("example-user-001", "ExampleOpen", "mixpanel", "home"),
            ("example-user-002", "ExampleClick", "mixpanel", "details"),
        ], rows
        print("PASS: Redis enqueue -> RQ worker -> event processor -> ClickHouse; 2 exact rows")
    finally:
        redis.close()
        client.close()


if __name__ == "__main__":
    main()
