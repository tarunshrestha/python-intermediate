from question import Question
from data import question_data
from quiz_brain import QuizBrain
from os import system
import random

no_of_ques = 12
right_ans = 0

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(qtext=question_text, qanswer=question_answer)
    question_bank.append(new_question)

system('cls')
quiz = QuizBrain(question_bank)
while quiz.isplaying():
    quiz.next_question()



