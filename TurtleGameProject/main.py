import turtle
from turtle import Turtle, Screen
import random

# from turtle import * // To import all the class

tim = Turtle()
tim.shape("turtle")
colors = ["red", "blue", "green", "yellow", "black"]
direction = [0, 90, 180, 270]
#tim.pensize(10)
tim.speed("fastest")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)

draw_spirograph(5)
# -----------for different shapes-------------------
# def shapes(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     shapes(i)

# -----------for moving forward and making a square-------------------
# time = 5
# def walk(name, state):
#     name.forward(1 + time)
#     name.penup()
#     name.forward(1 + time)
#     name.pendown()
#     name.right(90 - state)
#
#
# for a in range(50):
#     time += 1
#     walk(tim, 180)
#     print(time)

screen = Screen()
screen.exitonclick()
