
# asking the questions
# checking if the answer was correct
# checking if we're the end if the quiz

# creaate a quize brain class with two attributes: question number = 0 as default
# question_list

# also a method for helping the user go to the next question

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"That is correct! Well done.")
        else:
            print("That is wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current Score is {self.score} / {self.question_number} ")
        print("\n")
