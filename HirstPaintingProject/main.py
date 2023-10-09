import colorgram
import turtle as turtle_module
import random

# colors = colorgram.extract('prac.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

tim = turtle_module.Turtle()
tim.shape("turtle")
tim.penup()
tim.hideturtle()
turtle_module.colormode(255)
color_list = [(183, 158, 132), (224, 217, 209), (162, 178, 192), (195, 147, 160), (194, 207, 219),
            (124, 99, 63), (48, 32, 19), (151, 145, 81), (227, 207, 214), (157, 177, 162), (176, 191, 213),
            (211, 220, 215), (185, 97, 113), (220, 173, 186), (31, 92, 15), (66, 114, 51), (136, 78, 90),
            (57, 25, 31), (202, 197, 168), (131, 24, 36), (222, 175, 169), (22, 68, 11), (181, 103, 93),
            (70, 82, 25), (173, 198, 206), (65, 104, 133), (178, 200, 188), (114, 39, 31), (26, 30, 60),
            (108, 145, 95)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
no_of_dots = 100
for i in range(1, no_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()