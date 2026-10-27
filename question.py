class Question:
    """One Question in the quiz"""

    def __init__(self, question_text, answers, correct_answer):
        """Stores question text, answers and the correct answer"""
        self.question_text = question_text
        self.answers = answers
        self.correct_answer = correct_answer

    def is_correct(self, answer_choice):
        """Return True if correct"""
        return answer_choice == self.correct_answer