from turtle import Turtle

FONT =("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update()

    def update(self):
        self.write(f"Score:{self.score}", align="center", font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
