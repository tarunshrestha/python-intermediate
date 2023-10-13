from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

canplay =True
while canplay :
    time.sleep(ball.bspeed)
    screen.update()
    ball.move()

    # ball collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(0)

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print('Touched player')
        ball.bounce(1)

    if ball.xcor() > 380:
        ball.reset_position()
        score.point(0)

    if ball.xcor() < -380:
        ball.reset_position()
        score.point(1)

screen.exitonclick()