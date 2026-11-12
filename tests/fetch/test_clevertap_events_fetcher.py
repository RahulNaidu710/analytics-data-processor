from fetch.clevertap_events_fetcher import ClevertapEventsFetcher
from unittest.mock import MagicMock
from .clevertap_sample import response, cursor_response
from domain.datasource.models import Credential, CredentialType


class TestClevertapEventsFetcher:
    def setup_method(self):
        self.mock_response = response
        self.mock_cursor_response = cursor_response
        self.credential = Credential(
            type=CredentialType.API_KEY,
            accountId="TEST_ACCOUNTID_006",
            secret="TEST_CREDENTIAL_003",
        )
        self.event = "UTM Visited"

    def test_daily_data(self):
        self.fetcher = ClevertapEventsFetcher(self.credential, "20221122")

        self.fetcher.get_start_cursor = MagicMock(
            return_value=self.mock_cursor_response
        )
        self.fetcher.open = MagicMock(return_value=self.mock_response)

        for result in self.fetcher.fetch(self.event):
            if result:
                assert set(["profile", "session_props", "ts", "event_props"]).issubset(
                    set(result[0].keys())
                )
