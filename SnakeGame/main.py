from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

canplay = True
while canplay:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15: # pixel is less then we can know its collided.
        food.refresh()
        snake.extend()
        scoreboard.increase()
        print("size +1")


# wall collision
    if -280 > snake.head.xcor() or snake.head.xcor() > 280 or 280 < snake.head.ycor() or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        #canplay = False

# Body collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            print("Body touched")
            scoreboard.reset()
            snake.reset()

            #canplay = False


screen.exitonclick()
