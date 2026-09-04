from __future__ import annotations

import json
import unittest
from collections.abc import Mapping
from typing import Union, get_type_hints
from uuid import UUID

from urllib3.response import HTTPResponse

from x402api.api.orders_and_payments_api import OrdersAndPaymentsApi
from x402api.api_client import ApiClient
from x402api.api_response import ApiResponse
from x402api.models.payment_receipt import PaymentReceipt
from x402api.models.payment_receipt_status import PaymentReceiptStatus
from x402api.models.receipt_status_enum import ReceiptStatusEnum
from x402api.rest import RESTResponse


PAYMENT_ID = UUID("00000000-0000-4000-8000-000000000001")


class _StubApiClient(ApiClient):
    def __init__(self, status: int, payload: Mapping[str, object]) -> None:
        super().__init__()
        self.status = status
        self.payload = payload

    def call_api(self, *args, **kwargs) -> RESTResponse:
        del args, kwargs
        return RESTResponse(
            HTTPResponse(
                body=json.dumps(self.payload).encode("utf-8"),
                status=self.status,
                headers={"content-type": "application/json"},
                preload_content=True,
            )
        )


class PaymentReceiptResponseTests(unittest.TestCase):
    def test_public_return_annotations_include_both_success_models(self) -> None:
        expected = Union[PaymentReceipt, PaymentReceiptStatus]
        direct_hints = get_type_hints(
            OrdersAndPaymentsApi.payments_retrieve_receipt
        )
        info_hints = get_type_hints(
            OrdersAndPaymentsApi.payments_retrieve_receipt_with_http_info
        )

        self.assertEqual(direct_hints["return"], expected)
        self.assertEqual(info_hints["return"], ApiResponse[expected])

    def test_http_200_deserializes_as_signed_receipt(self) -> None:
        payload: dict[str, object] = {
            "id": str(PAYMENT_ID),
            "order_id": "00000000-0000-4000-8000-000000000002",
            "settlement_job_id": "00000000-0000-4000-8000-000000000003",
            "receipt": {"type": "x402api.payment-receipt"},
            "receipt_digest": "sha256:receipt",
            "signature": "signature",
            "signing_key_version": "v1",
            "eligible_alternatives": [],
            "fee_policy": None,
            "fee_evidence": None,
            "fee_quote_digest": None,
            "fee_quote_expires_at": None,
            "settlement_amount_atomic": "25000000",
            "gas_mode": "buyer_pays",
            "buyer_native_fee_atomic": "0",
            "sponsored_native_fee_atomic": None,
            "sponsored_native_symbol": None,
            "tenant_gas_charge_micros": None,
            "gas_sponsorship_evidence_digest": None,
            "created_at": "2026-09-04T00:00:01Z",
        }
        api = OrdersAndPaymentsApi(_StubApiClient(200, payload))

        receipt = api.payments_retrieve_receipt(id=PAYMENT_ID)
        response = api.payments_retrieve_receipt_with_http_info(id=PAYMENT_ID)

        assert isinstance(receipt, PaymentReceipt)
        self.assertEqual(receipt.id, PAYMENT_ID)
        self.assertEqual(receipt.settlement_amount_atomic, "25000000")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, PaymentReceipt)

    def test_http_202_deserializes_as_confirmation_status(self) -> None:
        payload: dict[str, object] = {
            "payment_id": str(PAYMENT_ID),
            "state": "confirming",
            "confirmed": True,
            "finalized": False,
            "confirmed_at": "2026-09-04T00:00:00Z",
            "finalized_at": None,
            "transaction": "0xabc",
            "network": "eip155:8453",
            "receipt_status": "pending_finality",
        }
        api = OrdersAndPaymentsApi(_StubApiClient(202, payload))

        status = api.payments_retrieve_receipt(id=PAYMENT_ID)
        response = api.payments_retrieve_receipt_with_http_info(id=PAYMENT_ID)

        assert isinstance(status, PaymentReceiptStatus)
        self.assertTrue(status.confirmed)
        self.assertFalse(status.finalized)
        self.assertEqual(status.receipt_status, ReceiptStatusEnum.PENDING_FINALITY)
        self.assertEqual(response.status_code, 202)
        self.assertIsInstance(response.data, PaymentReceiptStatus)


if __name__ == "__main__":
    unittest.main()
