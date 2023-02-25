class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        # self.question_num = ques_next

        current_answer = input(f"Q.{self.question_num}: {self.question_list[self.question_num].text} True/False : ")

        self.check_answer(current_answer, self.question_list[self.question_num].answer.lower())
        self.question_num += 1

    def check_answer(self, current_answer, correct_answer):
        if current_answer == correct_answer:
            self.score += 1
            print("Your answer is right!")
            print(f"Correct answer is :{correct_answer.capitalize()}")
            print(f"Your Score is: {self.score}/{self.question_num+1}")
        else:
            print("You got wrong!")
            print(f"Correct answer is: {correct_answer.capitalize()}")
            print(f"Your Score is: {self.score}/{self.question_num +1 }")

    def final_score(self):
        print("\nYou have completed the quiz")
        print(f"Your final score is: {self.score}")
