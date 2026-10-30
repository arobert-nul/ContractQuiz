import unittest
from question import Question


class TestQuestion(unittest.TestCase):
    """Tests whether question and answer works accurately"""

    def setUp(self):
        """Create a sample question before each test."""
        self.question = Question("What is the age range of the TCIAG contract?", ["13-18", "19-25", "19-45", "All Adults"], "A")

    def test_correct_answer_accepted(self):
        """Tests that the correct answer is accepted"""
        self.assertTrue(self.question.is_correct("A"))

    def test_incorrect_answer_accepted(self):
        """Tests that the wrong answer is not accepted"""
        self.assertFalse(self.question.is_correct("B"))        


if __name__ == "__main__":
    unittest.main()