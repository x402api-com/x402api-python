import unittest
from uuid import UUID

from x402api.api.programmatic_charges_api import ProgrammaticChargesApi


class _RecordingApiClient:
    def select_header_accept(self, values):
        return values[0]

    def param_serialize(self, **kwargs):
        return kwargs


class ChargePaymentSubmissionTests(unittest.TestCase):
    def test_serializes_one_signature_header_and_no_body(self):
        api = ProgrammaticChargesApi(api_client=_RecordingApiClient())
        charge_id = UUID("01a059a6-a521-700e-8499-ea7d8cd3d04b")

        request = api._charges_submit_payment_serialize(
            payment_signature="signed-artifact",
            charge_id=charge_id,
            _request_auth=None,
            _content_type=None,
            _headers=None,
            _host_index=0,
        )

        self.assertEqual(request["method"], "POST")
        self.assertEqual(
            request["resource_path"], "/v1/charges/{charge_id}/payments"
        )
        self.assertEqual(request["path_params"], {"charge_id": charge_id})
        self.assertEqual(
            request["header_params"]["PAYMENT-SIGNATURE"], "signed-artifact"
        )
        self.assertIsNone(request["body"])


if __name__ == "__main__":
    unittest.main()
