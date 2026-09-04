from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).parents[1]
SCRIPT = REPOSITORY_ROOT / "scripts" / "patch-receipt-response-types.py"
SPEC = importlib.util.spec_from_file_location(
    "patch_receipt_response_types", SCRIPT
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PatchReceiptResponseTypesTests(unittest.TestCase):
    def test_patch_is_exact_and_idempotent(self) -> None:
        patched = MODULE.TARGET.read_text(encoding="utf-8")
        unpatched = patched.replace(MODULE.PAYMENT_RECEIPT_STATUS_IMPORT, "")
        for generated, replacement in MODULE.RETURN_TYPE_REPLACEMENTS:
            unpatched = unpatched.replace(replacement, generated)

        self.assertEqual(MODULE.patch_source(unpatched), patched)
        self.assertEqual(MODULE.patch_source(patched), patched)

    def test_patch_fails_closed_if_202_response_contract_drifts(self) -> None:
        source = MODULE.TARGET.read_text(encoding="utf-8")
        drifted = source.replace(MODULE.STATUS_RESPONSE_MARKER, "", 1)

        with self.assertRaisesRegex(ValueError, "expected 3 occurrence"):
            MODULE.patch_source(drifted)

    def test_documentation_patch_is_exact_and_idempotent(self) -> None:
        patched = MODULE.DOCUMENTATION_TARGET.read_text(encoding="utf-8")
        unpatched = patched.replace(
            MODULE.PATCHED_DOCUMENTATION_SIGNATURE,
            MODULE.DOCUMENTATION_SIGNATURE,
        ).replace(MODULE.DOCUMENTATION_STATUS_IMPORT, "")
        unpatched = unpatched.replace(
            MODULE.PATCHED_DOCUMENTATION_RETURN_TYPE,
            MODULE.DOCUMENTATION_RETURN_TYPE,
        )

        self.assertEqual(MODULE.patch_documentation(unpatched), patched)
        self.assertEqual(MODULE.patch_documentation(patched), patched)

    def test_documentation_patch_fails_closed_if_202_contract_drifts(self) -> None:
        source = MODULE.DOCUMENTATION_TARGET.read_text(encoding="utf-8")
        drifted = source.replace(MODULE.DOCUMENTATION_202_MARKER, "", 1)

        with self.assertRaisesRegex(ValueError, "expected 1 occurrence"):
            MODULE.patch_documentation(drifted)


if __name__ == "__main__":
    unittest.main()
