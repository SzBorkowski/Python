import turtle
import random

timmy_the_turtle = turtle.Turtle()
colours = ["red", "green", "blue", "yellow", "violet", "black"]
moves = ["right(90)", "right(180)", "left(90)", "right(0)"]
turtle.colormode(255)

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

def square(turtle):
    turtle.pu()
    turtle.forward(50)
    turtle.left(90)
    turtle.pd()
    turtle.forward(50)
    for x in range(3):
        turtle.left(90)
        turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.pu()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.pd()

def dashline(t):
    for x in range(10):
        t.forward(10)
        t.pu()
        t.forward(10)
        t.pd()

def shapes(t):
    for x in range(3, 11):
        t.color(random.choice(colours))
        for y in range(x):
            t.right(360/x)
            t.forward(100)

def walk(t):
    t.pensize(10)
    while True:
        t.color(random_color())
        t.right(random.choice([0, 90, 180, 270]))
        t.forward(50)

def circles(t, angle):
    for x in range(int(360 / angle)):
        t.color(random_color())
        t.circle(100)
        t.setheading(timmy_the_turtle.heading() + angle)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r ,g, b)
    return color

timmy_the_turtle.speed("fastest")
#square(timmy_the_turtle)
#dashline(timmy_the_turtle)
#shapes(timmy_the_turtle)
#walk(timmy_the_turtle)
#circles(timmy_the_turtle, 5)

screen = turtle.Screen()
screen.exitonclick()
