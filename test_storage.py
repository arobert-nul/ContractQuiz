import os
import unittest
from storage import save_result, load_results

TEST_FILE = "test_results.csv"


class TestStorage(unittest.TestCase):
    """Tests result storage saving and loading"""

    def tearDown(self):
        """Delete the test file after each test."""
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_save_then_load(self):
        """Tests saving and then loading of a file"""
        save_result(TEST_FILE, "Michael", 3, 5)
        self.assertEqual(load_results(TEST_FILE), [['Michael', '3', '5']])

    def test_missing_file_returns_empty_list(self):
        """This tests the return if the list is empty"""
        self.assertEqual(load_results("missing_results"), [])


if __name__ == "__main__":
    unittest.main()