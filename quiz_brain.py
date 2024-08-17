class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = self.get_user_answer(f"Q.{self.question_number}: {current_question.text} [True/False]: ")
        self.check_answer(user_answer, current_question.answer)

    @staticmethod
    def get_user_answer(prompt):
        expected_answers = ['true', 'false']
        user_answer = input(prompt).lower().strip()

        while user_answer not in expected_answers:
            user_answer = input("Invalid Input. Only 'True' or 'False' accepted. Please try again: ").lower().strip()

        return user_answer

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That´s wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

