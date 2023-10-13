from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, 'up')
screen.onkey(r_paddle.go_down, 'down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')






canplay =True
while canplay :
    screen.update()

screen.exitonclick()