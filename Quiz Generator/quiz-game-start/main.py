from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
# Object containing questions and their answers
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

    # question_bank.append(q_object)


quiz = QuizBrain(question_bank)


while quiz.still_has_questions():

    quiz.next_question()

print("You've completed this quiz")
print(f"Your final score is {quiz.score} / {quiz.question_number}")
# put this on github.
