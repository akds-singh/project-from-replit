import question_model
import data
from quiz_brain import QuizBrain


question_bank = []
for item in data.question_data:
    ques_str = item['question']
    ans_str = item['correct_answer']
    question = question_model.Question(ques_str, ans_str)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

quiz.next_question()
while quiz.still_has_question():
    quiz.next_question()

quiz.final_score()