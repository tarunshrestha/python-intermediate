from turtle import Turtle

<<<<<<< HEAD
SPEED = 40
=======
>>>>>>> 2dc9f75dcdf109bd29f30cb0727c386557d7232d
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
<<<<<<< HEAD
        if 280 > self.ycor():
            new_y = self.ycor() + SPEED
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - SPEED
            self.goto(self.xcor(), new_y)
=======
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
>>>>>>> 2dc9f75dcdf109bd29f30cb0727c386557d7232d
