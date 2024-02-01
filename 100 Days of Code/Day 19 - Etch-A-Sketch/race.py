from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Bet", prompt="Pick a turtle (red, orange, yellow, green, blue, purple): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = 120
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-220, y=y)
    all_turtles.append(new_turtle)
    y -= 40

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print("You've won!")
            else:
                print(f"You've lost. Turtle with a {winning_color} color won.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
