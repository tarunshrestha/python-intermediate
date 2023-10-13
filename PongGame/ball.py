from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('blue')
        self.shape('circle')
        self.penup()
        self.x = 10
        self.y = 10
        self.bspeed = 0.1

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce(self, num):
        self.y *= -1
        if num == 1:
            self.x *= -1
            self.bspeed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.x *= -1
        self.bspeed = 0.1


