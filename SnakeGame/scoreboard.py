from turtle import Turtle
<<<<<<< HEAD
from typing import Tuple

#Read only
with open('Data.txt') as data:
     high_score = int(data.read())

FONT: Tuple[str, int, str] = ("Courier", 20, "normal")
#DATA = open('Data.txt')
#close = DATA.close()

=======

FONT =("Courier", 20, "normal")
>>>>>>> 2dc9f75dcdf109bd29f30cb0727c386557d7232d

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self.highscore = high_score
=======
>>>>>>> 2dc9f75dcdf109bd29f30cb0727c386557d7232d
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update()

    def update(self):
<<<<<<< HEAD
        self.clear()
        self.write(f"Score:{self.score} HighScore = {self.highscore}", align="center", font=FONT)
=======
        self.write(f"Score:{self.score}", align="center", font=FONT)
>>>>>>> 2dc9f75dcdf109bd29f30cb0727c386557d7232d

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

<<<<<<< HEAD
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('Data.txt', mode='w') as override:
                override.write(f'{self.highscore}')
        self.score = 0
        self.update()

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=FONT)
=======
    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
>>>>>>> 2dc9f75dcdf109bd29f30cb0727c386557d7232d
