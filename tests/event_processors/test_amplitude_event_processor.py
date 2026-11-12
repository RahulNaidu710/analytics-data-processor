import pandas as pd

from event_processors.amplitude_event_processor import AmplitudeEventProcessor


class TestAmplitudeEventProcessor:
    def setup_method(self):
        json = """
        {"$insert_id":"00000000-0000-4000-8000-000000000004","$insert_key":"00000000000000000000000000000003ee#422","$schema":13,"adid":null,"amplitude_attribution_ids":null,"amplitude_event_type":null,"amplitude_id":10001,"app":100001,"city":"EXAMPLE_VALUE_001","client_event_time":"2022-11-14 00:57:33.008000","client_upload_time":"2022-11-14 00:57:33.010000","country":"EXAMPLE_VALUE_002","data":{"group_ids":{},"group_first_event":{}},"data_type":"event","device_brand":null,"device_carrier":null,"device_family":"Android","device_id":"TEST_IDENTITY_001","device_manufacturer":null,"device_model":"Android","device_type":"Android","dma":null,"event_id":10002,"event_properties":{"anonymous_id":"00000000-0000-4000-8000-000000000006","event_source":"example-source","value":"user005@example.com","attribute_duplicated":"email","timestamp":"2022-11-14T00:57:32.907Z"},"event_time":"2022-11-14 00:57:33.008000","event_type":"user_duplicated","global_user_properties":{},"group_properties":{},"groups":{},"idfa":null,"ip_address":"192.0.2.1","is_attribution_event":false,"language":"English","library":"amplitude-js/5.2.2","location_lat":null,"location_lng":null,"os_name":"EXAMPLE_VALUE_003","os_version":"107","partner_id":null,"paying":null,"plan":{},"platform":"Web","processed_time":"2022-11-14 00:57:35.949636","region":"EXAMPLE_VALUE_004","sample_rate":null,"server_received_time":"2022-11-14 00:57:34.045000","server_upload_time":"2022-11-14 00:57:34.048000","session_id":10003,"source_id":null,"start_version":null,"user_creation_time":"2022-04-04 04:45:04.794000","user_id":"TEST_IDENTITY_002","user_properties":{"contact_number":"EXAMPLE_VALUE_005","email_verified":true,"referring_domain":"EXAMPLE_VALUE_006","marital_status":"EXAMPLE_VALUE_007","education_level":"EXAMPLE_VALUE_008","utm_source":"EXAMPLE_VALUE_009","city_permanent":"EXAMPLE_VALUE_010","first_name":"EXAMPLE_VALUE_011","home_phone":"EXAMPLE_VALUE_012","gender":"EXAMPLE_VALUE_013","anonymous_id":"00000000-0000-4000-8000-000000000007","net_salary":100,"city_current":"EXAMPLE_VALUE_010","initial_utm_source":"EXAMPLE_VALUE_009","email":"user006@example.com","user_id":"TEST_IDENTITY_002","company":"EXAMPLE_VALUE_014","address_permanent":"EXAMPLE_VALUE_015","resident_since_current":"EXAMPLE_VALUE_016","contact_name":"EXAMPLE_VALUE_017","mobile_number":"EXAMPLE_VALUE_018","address_current":"EXAMPLE_VALUE_015","zip_code_current":"EXAMPLE_VALUE_019","referrer":"EXAMPLE_VALUE_020","resident_type_permanent":"EXAMPLE_VALUE_021","timestamp":"EXAMPLE_VALUE_022","province_permanent":"EXAMPLE_VALUE_023","job_level":"EXAMPLE_VALUE_024","email_address":"user006@example.com","initial_referring_domain":"EXAMPLE_VALUE_025","initial_utm_campaign":"EXAMPLE_VALUE_026","zip_code_permanent":"EXAMPLE_VALUE_019","initial_utm_content":"EXAMPLE_VALUE_026","utm_medium":"EXAMPLE_VALUE_027","event_source":"example-source","initial_utm_medium":"EXAMPLE_VALUE_027","initial_referrer":"EXAMPLE_VALUE_029","resident_since_permanent":"EXAMPLE_VALUE_016","updated_date":100,"employee_id":"TEST_IDENTITY_003","resident_type_current":"EXAMPLE_VALUE_021","basic_salary":100,"bank_code":"EXAMPLE_VALUE_030","dependents_number":100,"middle_name":"EXAMPLE_VALUE_031","utm_campaign":"EXAMPLE_VALUE_026","last_name":"EXAMPLE_VALUE_032","anonymousId":"00000000-0000-4000-8000-000000000007","existing_loans":true,"employment_start_date_current":"EXAMPLE_VALUE_033","province_current":"EXAMPLE_VALUE_023","birth_place":"EXAMPLE_VALUE_034","spouse_first_name":"EXAMPLE_VALUE_017","phone":"EXAMPLE_VALUE_018","employment_type":"EXAMPLE_VALUE_035","utm_content":"EXAMPLE_VALUE_026","created_at":"EXAMPLE_VALUE_036","bank_account_number":"EXAMPLE_VALUE_018","job_title":"EXAMPLE_VALUE_037","relationship":"EXAMPLE_VALUE_038","id":"TEST_IDENTITY_002"},"uuid":"00000000-0000-4000-8000-000000000008","version_name":null}
        {"$insert_id":"00000000-0000-4000-8000-000000000009","$insert_key":"00000000000000000000000000000003ef#415","$schema":13,"adid":null,"amplitude_attribution_ids":null,"amplitude_event_type":null,"amplitude_id":10004,"app":100001,"city":"EXAMPLE_VALUE_039","client_event_time":"2022-11-14 00:57:32.668000","client_upload_time":"2022-11-14 00:57:32.670000","country":"EXAMPLE_VALUE_002","data":{"group_ids":{},"group_first_event":{}},"data_type":"event","device_brand":null,"device_carrier":null,"device_family":"Android","device_id":"TEST_IDENTITY_004","device_manufacturer":null,"device_model":"Android","device_type":"Android","dma":null,"event_id":10005,"event_properties":{"path":"/wcr","anonymous_id":"00000000-0000-4000-8000-00000000000b","name":"EXAMPLE_VALUE_040","event_source":"example-source","title":"Borrower Dashboard - Example Site","url":"https://app.example.com/example-1","timestamp":"2022-11-14T00:57:32.629Z"},"event_time":"2022-11-14 00:57:32.668000","event_type":"Viewed /wcr Page","global_user_properties":{},"group_properties":{},"groups":{},"idfa":null,"ip_address":"192.0.2.2","is_attribution_event":false,"language":"English","library":"amplitude-js/5.2.2","location_lat":null,"location_lng":null,"os_name":"EXAMPLE_VALUE_003","os_version":"107","partner_id":null,"paying":null,"plan":{},"platform":"Web","processed_time":"2022-11-14 00:57:37.156242","region":"EXAMPLE_VALUE_041","sample_rate":null,"server_received_time":"2022-11-14 00:57:34.186000","server_upload_time":"2022-11-14 00:57:34.189000","session_id":10006,"source_id":null,"start_version":null,"user_creation_time":"2022-11-04 03:05:41.855000","user_id":"TEST_IDENTITY_005","user_properties":{"referring_domain":"EXAMPLE_VALUE_025","event_source":"example-source","initial_referrer":"EXAMPLE_VALUE_020","first_name":"EXAMPLE_VALUE_042","anonymous_id":"00000000-0000-4000-8000-00000000000b","created_date":100,"email":"user007@example.com","user_id":"TEST_IDENTITY_005","middle_name":"EXAMPLE_VALUE_043","last_name":"EXAMPLE_VALUE_044","referrer":"EXAMPLE_VALUE_045","anonymousId":"00000000-0000-4000-8000-00000000000b","timestamp":"EXAMPLE_VALUE_046","phone":"EXAMPLE_VALUE_047","initial_referring_domain":"EXAMPLE_VALUE_006","id":"TEST_IDENTITY_005"},"uuid":"00000000-0000-4000-8000-00000000000c","version_name":null}
        {"$insert_id":"00000000-0000-4000-8000-00000000000d","$insert_key":"00000000000000000000000000000003f0#786","$schema":13,"adid":null,"amplitude_attribution_ids":null,"amplitude_event_type":null,"amplitude_id":10007,"app":100001,"city":"EXAMPLE_VALUE_048","client_event_time":"2022-11-14 00:57:35.755000","client_upload_time":"2022-11-14 00:57:36.329000","country":"EXAMPLE_VALUE_002","data":{"group_ids":{},"group_first_event":{}},"data_type":"event","device_brand":null,"device_carrier":null,"device_family":"Android","device_id":"TEST_IDENTITY_006","device_manufacturer":null,"device_model":"Android","device_type":"Android","dma":null,"event_id":10008,"event_properties":{"referrer":"https://app.example.com/example-2","path":"/login","anonymous_id":"00000000-0000-4000-8000-00000000000f","name":"EXAMPLE_VALUE_049","event_source":"example-source","url":"https://app.example.com/example-3","timestamp":"2022-11-14T00:57:35.693Z"},"event_time":"2022-11-14 00:57:35.755000","event_type":"Viewed /login Page","global_user_properties":{},"group_properties":{},"groups":{},"idfa":null,"ip_address":"192.0.2.3","is_attribution_event":false,"language":"English","library":"amplitude-js/5.2.2","location_lat":null,"location_lng":null,"os_name":"EXAMPLE_VALUE_003","os_version":"107","partner_id":null,"paying":null,"plan":{},"platform":"Web","processed_time":"2022-11-14 00:57:39.114864","region":"EXAMPLE_VALUE_023","sample_rate":null,"server_received_time":"2022-11-14 00:57:36.837000","server_upload_time":"2022-11-14 00:57:36.841000","session_id":10009,"source_id":null,"start_version":null,"user_creation_time":"2021-05-14 09:59:42.047000","user_id":"TEST_IDENTITY_007","user_properties":{"contact_number":"EXAMPLE_VALUE_050","email_verified":true,"referring_domain":"EXAMPLE_VALUE_025","marital_status":"EXAMPLE_VALUE_051","education_level":"EXAMPLE_VALUE_008","city_permanent":"EXAMPLE_VALUE_052","first_name":"EXAMPLE_VALUE_053","home_phone":"EXAMPLE_VALUE_054","gender":"EXAMPLE_VALUE_055","anonymous_id":"00000000-0000-4000-8000-000000000010","office_phone":"EXAMPLE_VALUE_054","net_salary":100,"city_current":"EXAMPLE_VALUE_052","credit_cards_number":100,"email":"user008@example.com","user_id":"TEST_IDENTITY_007","company":"EXAMPLE_VALUE_056","address_permanent":"EXAMPLE_VALUE_057","resident_since_current":"EXAMPLE_VALUE_058","contact_name":"EXAMPLE_VALUE_059","mobile_number":"EXAMPLE_VALUE_060","address_current":"EXAMPLE_VALUE_057","zip_code_current":"EXAMPLE_VALUE_061","referrer":"EXAMPLE_VALUE_029","resident_type_permanent":"EXAMPLE_VALUE_062","timestamp":"EXAMPLE_VALUE_063","province_permanent":"EXAMPLE_VALUE_064","job_level":"EXAMPLE_VALUE_065","email_address":"user008@example.com","initial_referring_domain":"EXAMPLE_VALUE_006","mothers_maiden_name":"EXAMPLE_VALUE_066","zip_code_permanent":"EXAMPLE_VALUE_061","event_source":"example-source","initial_referrer":"EXAMPLE_VALUE_020","car_owner":false,"resident_since_permanent":"EXAMPLE_VALUE_058","updated_date":100,"employee_id":"TEST_IDENTITY_008","resident_type_current":"EXAMPLE_VALUE_062","basic_salary":100,"bank_code":"EXAMPLE_VALUE_030","dependents_number":100,"middle_name":"EXAMPLE_VALUE_067","last_name":"EXAMPLE_VALUE_068","anonymousId":"00000000-0000-4000-8000-000000000010","existing_loans":false,"employment_start_date_current":"EXAMPLE_VALUE_069","province_current":"EXAMPLE_VALUE_064","birth_place":"EXAMPLE_VALUE_070","phone":"EXAMPLE_VALUE_060","employment_type":"EXAMPLE_VALUE_071","created_at":"EXAMPLE_VALUE_072","job_title":"EXAMPLE_VALUE_073","bank_account_number":"EXAMPLE_VALUE_060","relationship":"EXAMPLE_VALUE_074","id":"TEST_IDENTITY_007"},"uuid":"00000000-0000-4000-8000-000000000011","version_name":null}
        {"$insert_id":"00000000-0000-4000-8000-000000000012","$insert_key":"00000000000000000000000000000003f1#908","$schema":13,"adid":null,"amplitude_attribution_ids":null,"amplitude_event_type":null,"amplitude_id":10010,"app":100001,"city":"EXAMPLE_VALUE_075","client_event_time":"2022-11-14 00:57:36.233000","client_upload_time":"2022-11-14 00:57:36.235000","country":"EXAMPLE_VALUE_002","data":{"group_ids":{},"group_first_event":{}},"data_type":"event","device_brand":null,"device_carrier":null,"device_family":"Android","device_id":"TEST_IDENTITY_009","device_manufacturer":null,"device_model":"Android","device_type":"Android","dma":null,"event_id":10011,"event_properties":{"document_name":"EXAMPLE_VALUE_076","anonymous_id":"00000000-0000-4000-8000-000000000014","event_source":"example-source","application_id":"TEST_IDENTITY_010","timestamp":"2022-11-14T00:57:36.137Z"},"event_time":"2022-11-14 00:57:36.233000","event_type":"upload_file_bottom_sheet_viewed","global_user_properties":{},"group_properties":{},"groups":{},"idfa":null,"ip_address":"192.0.2.4","is_attribution_event":false,"language":"English","library":"amplitude-js/5.2.2","location_lat":null,"location_lng":null,"os_name":"EXAMPLE_VALUE_003","os_version":"103","partner_id":null,"paying":null,"plan":{},"platform":"Web","processed_time":"2022-11-14 00:57:38.958601","region":"EXAMPLE_VALUE_023","sample_rate":null,"server_received_time":"2022-11-14 00:57:37.262000","server_upload_time":"2022-11-14 00:57:37.265000","session_id":10012,"source_id":null,"start_version":null,"user_creation_time":"2022-10-13 15:21:01.934000","user_id":"TEST_IDENTITY_011","user_properties":{"referring_domain":"EXAMPLE_VALUE_025","event_source":"example-source","initial_referrer":"EXAMPLE_VALUE_077","first_name":"EXAMPLE_VALUE_078","anonymous_id":"00000000-0000-4000-8000-000000000014","created_date":100,"email":"user009@example.com","user_id":"TEST_IDENTITY_011","middle_name":"EXAMPLE_VALUE_079","last_name":"EXAMPLE_VALUE_080","referrer":"EXAMPLE_VALUE_081","anonymousId":"00000000-0000-4000-8000-000000000014","timestamp":"EXAMPLE_VALUE_082","phone":"EXAMPLE_VALUE_083","initial_referring_domain":"EXAMPLE_VALUE_025","id":"TEST_IDENTITY_011"},"uuid":"00000000-0000-4000-8000-000000000015","version_name":null}
        {"$insert_id":"00000000-0000-4000-8000-000000000016","$insert_key":"00000000000000000000000000000003f2#563","$schema":13,"adid":null,"amplitude_attribution_ids":null,"amplitude_event_type":null,"amplitude_id":10013,"app":100001,"city":"EXAMPLE_VALUE_039","client_event_time":"2022-11-14 00:57:35.597000","client_upload_time":"2022-11-14 00:57:35.599000","country":"EXAMPLE_VALUE_002","data":{"group_ids":{},"group_first_event":{}},"data_type":"event","device_brand":null,"device_carrier":null,"device_family":"Android","device_id":"TEST_IDENTITY_012","device_manufacturer":null,"device_model":"Android","device_type":"Android","dma":null,"event_id":10014,"event_properties":{"login_id":"user010@example.com","user_id":"TEST_IDENTITY_013","anonymous_id":"00000000-0000-4000-8000-000000000018","event_source":"example-source","type":"email","timestamp":"2022-11-14T00:57:34.779Z"},"event_time":"2022-11-14 00:57:35.597000","event_type":"user_login","global_user_properties":{},"group_properties":{},"groups":{},"idfa":null,"ip_address":"192.0.2.5","is_attribution_event":false,"language":"English","library":"amplitude-js/5.2.2","location_lat":null,"location_lng":null,"os_name":"EXAMPLE_VALUE_003","os_version":"96","partner_id":null,"paying":null,"plan":{},"platform":"Web","processed_time":"2022-11-14 00:57:39.031579","region":"EXAMPLE_VALUE_041","sample_rate":null,"server_received_time":"2022-11-14 00:57:37.458000","server_upload_time":"2022-11-14 00:57:37.459000","session_id":10015,"source_id":null,"start_version":null,"user_creation_time":"2022-11-14 00:56:35.427000","user_id":null,"user_properties":{"referring_domain":"EXAMPLE_VALUE_006","referrer":"EXAMPLE_VALUE_020","initial_referrer":"EXAMPLE_VALUE_020","initial_referring_domain":"EXAMPLE_VALUE_006"},"uuid":"00000000-0000-4000-8000-000000000019","version_name":null}
        """
        self.agg_df = pd.read_json(json, lines=True)
        self.processor = AmplitudeEventProcessor()

    def test_process_dataframe_user_id(self):
        """
        Should pick userId from device_id field if user_id is null
        """

        df = self.processor.process_dataframe(self.agg_df)
        assert df.userId.to_list() == [
            "TEST_IDENTITY_002",
            "TEST_IDENTITY_005",
            "TEST_IDENTITY_007",
            "TEST_IDENTITY_011",
            "TEST_IDENTITY_012",
        ]

    def test_process_dataframe_timestamp(self):
        """
        Should pick event_time as timestamp field
        """

        df = self.processor.process_dataframe(self.agg_df)
        assert df.timestamp.to_list() == [
            "2022-11-14 00:57:33",
            "2022-11-14 00:57:32",
            "2022-11-14 00:57:35",
            "2022-11-14 00:57:36",
            "2022-11-14 00:57:35",
        ]

    def test_process_dataframe_event_name(self):
        """
        Should pick event_type as eventName field
        """

        df = self.processor.process_dataframe(self.agg_df)
        assert df.eventName.to_list() == [
            "user_duplicated",
            "Viewed /wcr Page",
            "Viewed /login Page",
            "upload_file_bottom_sheet_viewed",
            "user_login",
        ]

    def test_process_dataframe_properties(self):
        """
        Should keep all the incoming fields in properties field, flattened to the same level with dot separator
        """

        df = self.processor.process_dataframe(self.agg_df)
        assert set(
            [
                "app",
                "city",
                "country",
                "data.group_ids",
                "data.group_first_event",
                "data_type",
                "device_brand",
                "device_carrier",
                "device_family",
                "device_id",
                "device_manufacturer",
                "device_model",
                "device_type",
                "dma",
                "event_id",
                "event_properties.anonymous_id",
                "event_properties.event_source",
                "event_properties.value",
                "event_properties.attribute_duplicated",
                "event_properties.timestamp",
                "event_time",
                "event_type",
                "ip_address",
                "is_attribution_event",
                "language",
                "location_lat",
                "location_lng",
                "os_name",
                "os_version",
                "partner_id",
                "paying",
                "plan",
                "platform",
                "processed_time",
                "region",
                "sample_rate",
                "server_received_time",
                "server_upload_time",
                "session_id",
                "source_id",
                "start_version",
                "user_creation_time",
                "user_id",
                "user_properties.contact_number",
                "user_properties.email_verified",
                "user_properties.referring_domain",
                "user_properties.marital_status",
                "user_properties.education_level",
                "user_properties.utm_source",
                "user_properties.city_permanent",
                "user_properties.first_name",
                "user_properties.home_phone",
                "user_properties.gender",
                "user_properties.anonymous_id",
                "user_properties.net_salary",
                "user_properties.city_current",
                "user_properties.initial_utm_source",
                "user_properties.email",
                "user_properties.user_id",
                "user_properties.company",
                "user_properties.address_permanent",
                "user_properties.resident_since_current",
                "user_properties.contact_name",
                "user_properties.mobile_number",
                "user_properties.address_current",
                "user_properties.zip_code_current",
                "user_properties.referrer",
                "user_properties.resident_type_permanent",
                "user_properties.timestamp",
                "user_properties.province_permanent",
                "user_properties.job_level",
                "user_properties.email_address",
                "user_properties.initial_referring_domain",
                "user_properties.initial_utm_campaign",
                "user_properties.zip_code_permanent",
                "user_properties.initial_utm_content",
                "user_properties.utm_medium",
                "user_properties.event_source",
                "user_properties.initial_utm_medium",
                "user_properties.initial_referrer",
                "user_properties.resident_since_permanent",
                "user_properties.updated_date",
                "user_properties.employee_id",
                "user_properties.resident_type_current",
                "user_properties.basic_salary",
                "user_properties.bank_code",
                "user_properties.dependents_number",
                "user_properties.middle_name",
                "user_properties.utm_campaign",
                "user_properties.last_name",
                "user_properties.anonymousId",
                "user_properties.existing_loans",
                "user_properties.employment_start_date_current",
                "user_properties.province_current",
                "user_properties.birth_place",
                "user_properties.spouse_first_name",
                "user_properties.phone",
                "user_properties.employment_type",
                "user_properties.utm_content",
                "user_properties.created_at",
                "user_properties.bank_account_number",
                "user_properties.job_title",
                "user_properties.relationship",
                "user_properties.id",
                "uuid",
                "version_name",
                "event_properties.path",
                "event_properties.name",
                "event_properties.title",
                "event_properties.url",
                "user_properties.created_date",
                "event_properties.referrer",
                "user_properties.office_phone",
                "user_properties.credit_cards_number",
                "user_properties.mothers_maiden_name",
                "user_properties.car_owner",
                "event_properties.document_name",
                "event_properties.application_id",
                "event_properties.login_id",
                "event_properties.user_id",
                "event_properties.type",
            ]
        ).issubset(set(df.properties.to_list()[0].keys()))
