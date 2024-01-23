from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

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

dashline(timmy_the_turtle)

screen = Screen()
screen.exitonclick()
