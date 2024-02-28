from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.pu()
            new_car.setposition(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def drive(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def faster(self):
        pass
