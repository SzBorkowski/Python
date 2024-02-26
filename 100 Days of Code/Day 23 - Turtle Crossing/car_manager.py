from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.setposition(300, random.randint(-250, 250))
        self.setheading(180)
        self.speed = STARTING_MOVE_DISTANCE

    def drive(self):
        self.forward(self.speed)

    def faster(self):
        self.speed += MOVE_INCREMENT
