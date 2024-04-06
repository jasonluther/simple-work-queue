'''
Simple test to get test infrastructure up and running. Just import the module.
'''
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import src
import src.simple_work_queue

def test_import():
    assert src.simple_work_queue is not None