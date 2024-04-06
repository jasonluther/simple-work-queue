"""
Simple test to get test infrastructure up and running. Just import the module.
"""

import unittest
import sys
import tests # I don't know why this is needed to make tests run in vscode.
import simple_work_queue


class TestImport(unittest.TestCase):
    def test_module_in_modules_list(self):
        modules_list = sys.modules.keys()
        self.assertIn("simple_work_queue", modules_list)
