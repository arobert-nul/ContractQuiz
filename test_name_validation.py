import unittest
from name_validation import validate_name


class TestValidateName(unittest.TestCase):
    """Tests for validate_name function"""

    def test_name_valid(self):
        """A name is accepted"""
        self.assertTrue(validate_name("Michael"))

    def test_name_spaces_valid(self):
           """A name with extra spaces is accepted"""
           self.assertTrue(validate_name("Michael     "))

    def test_name_rejected(self):
           """No name is rejected"""
           self.assertFalse(validate_name(""))

if __name__ == "__main__":
    unittest.main()