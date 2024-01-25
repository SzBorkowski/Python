# import colorgram
#
# getting colors from an image
# rgb_colors = []
# colors = colorgram.extract("image.jpeg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle
import random

color_list = [(205, 159, 87), (57, 88, 129), (142, 91, 42), (221, 206, 110),
              (136, 27, 49), (136, 174, 198), (155, 49, 85), (44, 54, 104),
              (167, 158, 43), (131, 187, 145), (82, 20, 43), (37, 42, 66),
              (188, 141, 166), (182, 95, 111), (89, 117, 175), (91, 155, 93),
              (57, 38, 33), (79, 152, 164), (196, 81, 71), (58, 121, 116),
              (77, 73, 46), (47, 74, 73), (219, 174, 188), (164, 201, 213),
              (178, 189, 213), (169, 206, 173)]

turtle.colormode(255)
t = turtle.Turtle()
t.pensize(20)
t.speed("fastest")
t.pu()
t.setheading(225)
t.forward(300)
t.setheading(0)
t.hideturtle()

for x in range(10):
    for y in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.backward(500)

screen = turtle.Screen()
screen.exitonclick()
