import unittest
import os
from io import StringIO
from count_to_n import count_to_n
import sys

class Test(unittest.TestCase):
    def test_count_to_n(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        count_to_n(5)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "1\n2\n3\n4\n5")

        captured_output = StringIO()
        sys.stdout = captured_output
        count_to_n(3)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "1\n2\n3")

    def test_file_exists(self):
        file_name = self.__module__.split(".")[-1] + ".py"
        self.assertTrue(os.path.isfile(file_name), f"{file_name} does not exist
