'''
Simple test to get test infrastructure up and running. Just import the module.
'''
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import simple_work_queue

class TestImport(unittest.TestCase):
    def test_module_in_modules_list(self):
        modules_list = sys.modules.keys()
        self.assertIn('simple_work_queue', modules_list)
    