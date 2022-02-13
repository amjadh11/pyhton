from main import *
import unittest


class TestMain(unittest.TestCase):
    def test_inputs(self):
        self.assertRaises(TypeError, read_write_files, True)
