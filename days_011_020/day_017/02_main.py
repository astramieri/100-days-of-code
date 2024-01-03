from data import question_data
from question_model import Question

question_bank = []

for qst in question_data:
    question_bank.append(Question(qst["text"], qst["answer"]))

for qst in question_bank:
    print(f"Question ({qst.text}, {qst.answer})")