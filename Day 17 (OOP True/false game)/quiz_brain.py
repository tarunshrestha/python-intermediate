class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.correct_ans = 0

    def isplaying(self):
        if self.question_number < len(self.question_list):  # return self.question_number < len(self.question_list)
            return True
        else:
            if 8 < self.correct_ans > 4:
                print("You completed with barely pass marks.")
            elif self.correct_ans > 8:
                print("Congrats in completing with Excellent score.")
            else:
                print("Go and read you need more practice.")
            print(f"Number of correct answer: {self.correct_ans} out of {self.question_number}")
            return False

    def next_question(self):
        current_ques = self.question_list[self.question_number]
        correct_ans = current_ques.answer.lower()
        self.question_number += 1
        ask = input(f"Q.{self.question_number}: {current_ques.text} (True/False):").lower()
        self.check_ans(ask, correct_ans)
        # incase i want to delete: del current_ques

    def check_ans(self, player_ans, correct_ans):
        if player_ans != correct_ans:
            print("Wrong answer.")
            print(f"Number of correct answer: {self.correct_ans} / {self.question_number}\n")
        else:
            self.correct_ans += 1
            print("Correct answer")
            print(f"Number of correct answer: {self.correct_ans} / {self.question_number} \n")
