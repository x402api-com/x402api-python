from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "write-release-manifest.py"
SPEC = importlib.util.spec_from_file_location("write_release_manifest", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ReleaseManifestTests(unittest.TestCase):
    def test_manifest_binds_both_contracts_to_the_exact_source(self) -> None:
        import tempfile

        document = {"openapi": "3.0.3", "info": {"version": "1.2.0"}, "paths": {}}
        with tempfile.TemporaryDirectory() as temporary:
            public = Path(temporary) / "public.json"
            sdk = Path(temporary) / "sdk.json"
            public.write_text(json.dumps(document))
            sdk.write_text(json.dumps(document))
            manifest = MODULE.build_manifest(
                public, sdk, "1.2.0", "a" * 40, MODULE.digest(document)
            )

        self.assertEqual(manifest["source_revision"], "a" * 40)
        self.assertEqual(manifest["openapi_sha256"], MODULE.digest(document))
        self.assertEqual(manifest["sdk_openapi_sha256"], MODULE.digest(document))

    def test_manifest_rejects_contract_substitution(self) -> None:
        import tempfile

        document = {"openapi": "3.0.3", "info": {"version": "1.2.0"}, "paths": {}}
        with tempfile.TemporaryDirectory() as temporary:
            public = Path(temporary) / "public.json"
            sdk = Path(temporary) / "sdk.json"
            public.write_text(json.dumps(document))
            sdk.write_text(json.dumps(document))
            with self.assertRaisesRegex(ValueError, "digest"):
                MODULE.build_manifest(
                    public, sdk, "1.2.0", "a" * 40, "sha256:" + "0" * 64
                )
