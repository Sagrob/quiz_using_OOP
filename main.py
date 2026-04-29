from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_Bank = []

for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(question_text, question_answer)
    question_Bank.append(new_question)

quiz = QuizBrain(question_Bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")