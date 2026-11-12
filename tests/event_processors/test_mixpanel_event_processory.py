import pandas as pd
from event_processors.mixpanel_event_processor import MixPanelEventProcessor


class TestMixpanelEventProcessor:
    def setup_method(self):
        self.events_data = """
        {"event":"Login","properties":{"time":1666026662,"distinct_id":"user003@example.com","$app_build_number":"5004","$app_release":"5004","$app_version":"1.5.6","$app_version_string":"1.5.6","$bluetooth_enabled":false,"$bluetooth_version":"ble","$brand":"realme","$carrier":"EXAMPLE_VALUE_001","$city":"EXAMPLE_VALUE_002","$device_id":"00000000-0000-4000-8000-000000000001","$had_persisted_distinct_id":false,"$has_nfc":false,"$has_telephone":true,"$insert_id":"TEST_IDENTITY_014","$lib_version":"1.6.0","$manufacturer":"realme","$model":"RMX2193","$mp_api_endpoint":"api.mixpanel.com","$mp_api_timestamp_ms":1666006899493,"$os":"Android","$os_version":"11","$region":"EXAMPLE_VALUE_003","$screen_dpi":320,"$screen_height":1448,"$screen_width":720,"$user_id":"user003@example.com","$wifi":true,"login_method":"Google","mp_country_code":"EXAMPLE_VALUE_004","mp_lib":"flutter","mp_processing_time_ms":1666006900267}}
        {"event":"Chapter_Click","properties":{"time":1666026700,"distinct_id":"user003@example.com","$app_build_number":"5004","$app_release":"5004","$app_version":"1.5.6","$app_version_string":"1.5.6","$bluetooth_enabled":false,"$bluetooth_version":"ble","$brand":"realme","$carrier":"EXAMPLE_VALUE_001","$city":"EXAMPLE_VALUE_002","$device_id":"00000000-0000-4000-8000-000000000001","$had_persisted_distinct_id":false,"$has_nfc":false,"$has_telephone":true,"$insert_id":"TEST_IDENTITY_015","$lib_version":"1.6.0","$manufacturer":"realme","$model":"RMX2193","$mp_api_endpoint":"api.mixpanel.com","$mp_api_timestamp_ms":1666006922484,"$os":"Android","$os_version":"11","$region":"EXAMPLE_VALUE_003","$screen_dpi":320,"$screen_height":1448,"$screen_width":720,"$user_id":"user003@example.com","$wifi":true,"chapter_name":"EXAMPLE_VALUE_005","mp_country_code":"EXAMPLE_VALUE_004","mp_lib":"flutter","mp_processing_time_ms":1666006922904}}
        {"event":"Video_Open","properties":{"time":1665968171,"distinct_id":"user004@example.com","$app_build_number":"5004","$app_release":"5004","$app_version":"1.5.6","$app_version_string":"1.5.6","$bluetooth_enabled":false,"$bluetooth_version":"ble","$brand":"TECNO","$carrier":"EXAMPLE_VALUE_006","$city":"EXAMPLE_VALUE_007","$device_id":"00000000-0000-4000-8000-000000000002","$had_persisted_distinct_id":false,"$has_nfc":false,"$has_telephone":true,"$insert_id":"TEST_IDENTITY_016","$lib_version":"1.6.0","$manufacturer":"TECNO","$model":"TECNO KH6","$mp_api_endpoint":"api.mixpanel.com","$mp_api_timestamp_ms":1665948432587,"$os":"Android","$os_version":"12","$region":"EXAMPLE_VALUE_008","$screen_dpi":320,"$screen_height":1539,"$screen_width":720,"$user_id":"user004@example.com","$wifi":false,"chapter_name":"EXAMPLE_VALUE_009","mp_country_code":"EXAMPLE_VALUE_010","mp_lib":"flutter","mp_processing_time_ms":1665948432615,"topic_name":"EXAMPLE_VALUE_011","uid":"EXAMPLE_USER_001"}}
        {"event":"$ae_session","properties":{"time":1665968375,"distinct_id":"user004@example.com","$ae_session_length":28.5,"$app_build_number":"5004","$app_release":"5004","$app_version":"1.5.6","$app_version_string":"1.5.6","$bluetooth_enabled":false,"$bluetooth_version":"ble","$brand":"TECNO","$carrier":"EXAMPLE_VALUE_006","$city":"EXAMPLE_VALUE_007","$device_id":"00000000-0000-4000-8000-000000000002","$had_persisted_distinct_id":false,"$has_nfc":false,"$has_telephone":true,"$insert_id":"TEST_IDENTITY_017","$lib_version":"1.6.0","$manufacturer":"TECNO","$model":"TECNO KH6","$mp_api_endpoint":"api.mixpanel.com","$mp_api_timestamp_ms":1665948576488,"$os":"Android","$os_version":"12","$region":"EXAMPLE_VALUE_008","$screen_dpi":320,"$screen_height":1539,"$screen_width":720,"$user_id":"user004@example.com","$wifi":false,"mp_country_code":"EXAMPLE_VALUE_010","mp_lib":"flutter","mp_processing_time_ms":1665948577075}}
        {"event":"$ae_first_open","properties":{"time":1665986037,"distinct_id":"00000000-0000-4000-8000-000000000003","$app_build_number":"5004","$app_release":"5004","$app_version":"1.5.6","$app_version_string":"1.5.6","$bluetooth_enabled":false,"$bluetooth_version":"ble","$brand":"OPPO","$carrier":"EXAMPLE_VALUE_012","$device_id":"00000000-0000-4000-8000-000000000003","$had_persisted_distinct_id":false,"$has_nfc":false,"$has_telephone":true,"$insert_id":"TEST_IDENTITY_018","$lib_version":"1.6.0","$manufacturer":"OPPO","$model":"CPH2015","$mp_api_endpoint":"api.mixpanel.com","$mp_api_timestamp_ms":1665966274970,"$os":"Android","$os_version":"9","$screen_dpi":320,"$screen_height":1544,"$screen_width":720,"$wifi":true,"mp_country_code":"EXAMPLE_VALUE_004","mp_lib":"flutter","mp_processing_time_ms":1665966275017}}
        """
        self.processor = MixPanelEventProcessor()

    def test_process_user_id(self):
        """
        Should pick properties.distinct_id as userId field
        """

        df = self.processor.process(self.events_data)
        assert df.userId.to_list() == [
            "user003@example.com",
            "user003@example.com",
            "user004@example.com",
            "user004@example.com",
            "00000000-0000-4000-8000-000000000003",
        ]

    def test_process_timestamp(self):
        """
        Should pick properties.time as timestamp field
        """

        df = self.processor.process(self.events_data)
        assert df.timestamp.to_list() == [
            "2022-10-17 17:11:02",
            "2022-10-17 17:11:40",
            "2022-10-17 00:56:11",
            "2022-10-17 00:59:35",
            "2022-10-17 05:53:57",
        ]

    def test_process_event_name(self):
        """
        Should pick event as eventName field
        """

        df = self.processor.process(self.events_data)
        assert df.eventName.to_list() == [
            "Login",
            "Chapter_Click",
            "Video_Open",
            "$ae_session",
            "$ae_first_open",
        ]

    def test_process_properties(self):
        """
        Should keep all the incoming fields in properties field, flattened to the same level with dot separator
        """
        df = self.processor.process(self.events_data)
        assert [
            "event",
            "properties.time",
            "properties.distinct_id",
            "properties.$app_build_number",
            "properties.$app_release",
            "properties.$app_version",
            "properties.$app_version_string",
            "properties.$bluetooth_enabled",
            "properties.$bluetooth_version",
            "properties.$brand",
            "properties.$carrier",
            "properties.$city",
            "properties.$device_id",
            "properties.$had_persisted_distinct_id",
            "properties.$has_nfc",
            "properties.$has_telephone",
            "properties.$insert_id",
            "properties.$lib_version",
            "properties.$manufacturer",
            "properties.$model",
            "properties.$mp_api_endpoint",
            "properties.$mp_api_timestamp_ms",
            "properties.$os",
            "properties.$os_version",
            "properties.$region",
            "properties.$screen_dpi",
            "properties.$screen_height",
            "properties.$screen_width",
            "properties.$user_id",
            "properties.$wifi",
            "properties.login_method",
            "properties.mp_country_code",
            "properties.mp_lib",
            "properties.mp_processing_time_ms",
            "properties.chapter_name",
            "properties.topic_name",
            "properties.uid",
            "properties.$ae_session_length",
        ] == list(df.properties.to_list()[0].keys())
