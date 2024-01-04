from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for qst in question_data:
    question_bank.append(Question(qst["text"], qst["answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

quiz_brain.final_score()
