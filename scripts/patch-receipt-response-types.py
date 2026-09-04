#!/usr/bin/env python3
"""Patch the generated receipt endpoint's multi-status return annotation."""

from __future__ import annotations

import ast
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
TARGET = REPOSITORY_ROOT / "x402api" / "api" / "orders_and_payments_api.py"
DOCUMENTATION_TARGET = REPOSITORY_ROOT / "docs" / "OrdersAndPaymentsApi.md"

PAYMENT_RECEIPT_IMPORT = (
    "from x402api.models.payment_receipt import PaymentReceipt\n"
)
PAYMENT_RECEIPT_STATUS_IMPORT = (
    "from x402api.models.payment_receipt_status import PaymentReceiptStatus\n"
)
STATUS_RESPONSE_MARKER = "            '202': \"PaymentReceiptStatus\",\n"
DOCUMENTATION_SIGNATURE = "> PaymentReceipt payments_retrieve_receipt(id)"
PATCHED_DOCUMENTATION_SIGNATURE = (
    "> Union[PaymentReceipt, PaymentReceiptStatus] "
    "payments_retrieve_receipt(id)"
)
DOCUMENTATION_STATUS_IMPORT = (
    "from x402api.models.payment_receipt_status import PaymentReceiptStatus\n"
)
DOCUMENTATION_RETURN_TYPE = "[**PaymentReceipt**](PaymentReceipt.md)"
PATCHED_DOCUMENTATION_RETURN_TYPE = (
    "[**PaymentReceipt**](PaymentReceipt.md) or "
    "[**PaymentReceiptStatus**](PaymentReceiptStatus.md)"
)
DOCUMENTATION_202_MARKER = (
    "**202** | Payment status while the signed finalized receipt is pending."
)

RETURN_TYPE_REPLACEMENTS = (
    (
        "    ) -> PaymentReceipt:\n",
        "    ) -> Union[PaymentReceipt, PaymentReceiptStatus]:\n",
    ),
    (
        "    ) -> ApiResponse[PaymentReceipt]:\n",
        (
            "    ) -> "
            "ApiResponse[Union[PaymentReceipt, PaymentReceiptStatus]]:\n"
        ),
    ),
)

EXPECTED_RETURN_ANNOTATIONS = {
    "payments_retrieve_receipt": "Union[PaymentReceipt, PaymentReceiptStatus]",
    "payments_retrieve_receipt_with_http_info": (
        "ApiResponse[Union[PaymentReceipt, PaymentReceiptStatus]]"
    ),
    "payments_retrieve_receipt_without_preload_content": "RESTResponseType",
}


def _require_count(source: str, marker: str, expected: int) -> None:
    actual = source.count(marker)
    if actual != expected:
        raise ValueError(
            f"generated receipt API drifted: expected {expected} occurrence(s) "
            f"of {marker!r}, found {actual}"
        )


def _verify_ast(source: str) -> None:
    module = ast.parse(source)
    api_classes = [
        node
        for node in module.body
        if isinstance(node, ast.ClassDef)
        and node.name == "OrdersAndPaymentsApi"
    ]
    if len(api_classes) != 1:
        raise ValueError(
            "generated receipt API drifted: expected exactly one "
            f"OrdersAndPaymentsApi class, found {len(api_classes)}"
        )
    api_class = api_classes[0]

    methods = [
        node
        for node in api_class.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    for method_name, expected in EXPECTED_RETURN_ANNOTATIONS.items():
        matches = [method for method in methods if method.name == method_name]
        if len(matches) != 1 or matches[0].returns is None:
            raise ValueError(
                f"generated receipt API drifted: expected exactly one "
                f"annotated {method_name} method"
            )
        method = matches[0]
        return_annotation = method.returns
        assert return_annotation is not None
        actual = ast.unparse(return_annotation)
        if actual != expected:
            raise ValueError(
                f"generated receipt API drifted: {method_name} returns "
                f"{actual!r}, expected {expected!r}"
            )

        status_responses = 0
        for node in ast.walk(method):
            if not isinstance(node, ast.Dict):
                continue
            for key, value in zip(node.keys, node.values):
                if (
                    isinstance(key, ast.Constant)
                    and key.value == "202"
                    and isinstance(value, ast.Constant)
                    and value.value == "PaymentReceiptStatus"
                ):
                    status_responses += 1
        if status_responses != 1:
            raise ValueError(
                f"generated receipt API drifted: expected {method_name} to "
                "map HTTP 202 to PaymentReceiptStatus exactly once"
            )


def patch_source(source: str) -> str:
    """Return the exact patched source, rejecting unknown generator output."""
    _require_count(source, STATUS_RESPONSE_MARKER, 3)
    _require_count(source, PAYMENT_RECEIPT_IMPORT, 1)

    status_import_count = source.count(PAYMENT_RECEIPT_STATUS_IMPORT)
    if status_import_count == 0:
        source = source.replace(
            PAYMENT_RECEIPT_IMPORT,
            PAYMENT_RECEIPT_IMPORT + PAYMENT_RECEIPT_STATUS_IMPORT,
            1,
        )
    elif status_import_count != 1:
        raise ValueError(
            "generated receipt API drifted: expected at most one "
            "PaymentReceiptStatus import"
        )

    for generated, patched in RETURN_TYPE_REPLACEMENTS:
        generated_count = source.count(generated)
        patched_count = source.count(patched)
        if (generated_count, patched_count) == (1, 0):
            source = source.replace(generated, patched, 1)
        elif (generated_count, patched_count) != (0, 1):
            raise ValueError(
                "generated receipt API drifted: expected exactly one "
                f"unpatched or patched annotation for {patched.strip()!r}; "
                f"found {generated_count} and {patched_count}"
            )

    _require_count(source, PAYMENT_RECEIPT_STATUS_IMPORT, 1)
    _require_count(source, STATUS_RESPONSE_MARKER, 3)
    for generated, patched in RETURN_TYPE_REPLACEMENTS:
        _require_count(source, generated, 0)
        _require_count(source, patched, 1)
    _verify_ast(source)
    return source


def patch_documentation(source: str) -> str:
    """Patch the generated endpoint documentation, rejecting drift."""
    generated_signature_count = source.count(DOCUMENTATION_SIGNATURE)
    patched_signature_count = source.count(PATCHED_DOCUMENTATION_SIGNATURE)
    if (generated_signature_count, patched_signature_count) == (1, 0):
        source = source.replace(
            DOCUMENTATION_SIGNATURE,
            PATCHED_DOCUMENTATION_SIGNATURE,
            1,
        )
    elif (generated_signature_count, patched_signature_count) != (0, 1):
        raise ValueError("generated receipt documentation signature drifted")

    _require_count(source, "from x402api.models.payment_receipt import PaymentReceipt\n", 1)
    status_import_count = source.count(DOCUMENTATION_STATUS_IMPORT)
    if status_import_count == 0:
        source = source.replace(
            "from x402api.models.payment_receipt import PaymentReceipt\n",
            (
                "from x402api.models.payment_receipt import PaymentReceipt\n"
                + DOCUMENTATION_STATUS_IMPORT
            ),
            1,
        )
    elif status_import_count != 1:
        raise ValueError("generated receipt documentation status import drifted")

    patched_return_count = source.count(PATCHED_DOCUMENTATION_RETURN_TYPE)
    if patched_return_count == 0:
        _require_count(source, DOCUMENTATION_RETURN_TYPE, 1)
        source = source.replace(
            DOCUMENTATION_RETURN_TYPE,
            PATCHED_DOCUMENTATION_RETURN_TYPE,
            1,
        )
    elif patched_return_count != 1:
        raise ValueError("generated receipt documentation return type drifted")

    _require_count(source, PATCHED_DOCUMENTATION_SIGNATURE, 1)
    _require_count(source, DOCUMENTATION_STATUS_IMPORT, 1)
    _require_count(source, PATCHED_DOCUMENTATION_RETURN_TYPE, 1)
    _require_count(source, DOCUMENTATION_202_MARKER, 1)
    return source


def patch_file(path: Path = TARGET) -> bool:
    source = path.read_text(encoding="utf-8")
    patched = patch_source(source)
    if patched == source:
        return False
    path.write_text(patched, encoding="utf-8")
    return True


def patch_documentation_file(path: Path = DOCUMENTATION_TARGET) -> bool:
    source = path.read_text(encoding="utf-8")
    patched = patch_documentation(source)
    if patched == source:
        return False
    path.write_text(patched, encoding="utf-8")
    return True


def main() -> None:
    patch_file()
    patch_documentation_file()


if __name__ == "__main__":
    main()
