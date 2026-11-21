"""
Simple test to get test infrastructure up and running. Just import the module.
"""

import importlib
import sys
import unittest

import tests  # noqa: F401 - I don't know why this is needed to make tests run in vscode.


class TestImport(unittest.TestCase):
    def test_module_in_modules_list(self):
        importlib.import_module("simple_work_queue")
        modules_list = sys.modules.keys()
        self.assertIn("simple_work_queue", modules_list)
