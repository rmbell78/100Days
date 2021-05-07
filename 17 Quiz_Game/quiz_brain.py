class QuizBrain:
    def __init__(self, l):
        self.question_number = 0
        self.question_list = l
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You Got it!')
            self.score += 1
        else:
            print("That's Wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your Score: {self.score}/{self.question_number + 1}")
        print('\n')

