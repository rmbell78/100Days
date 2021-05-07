from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i.get('question'), i.get('correct_answer')))

brain = QuizBrain(question_bank)
while brain.still_has_questions():
    brain.next_question()

print("Game Over!")
print(f"Your Final Score: {brain.score}/{len(question_bank)}")

