from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.spawn_cars()

    def spawn_cars(self):
        for color in COLORS:
            self.add_car(color)

    def add_car(self, color):
        new_car = Turtle("square")
        new_car.color(color)
        new_car.pu()
        new_car.setposition(300, random.randint(-250, 250))
        new_car.setheading(180)
        self.cars.append(new_car)

    def drive(self):
        for car_num in range(len(self.cars) - 1, 0, -1):
            self.cars[car_num].forward(STARTING_MOVE_DISTANCE)

    def faster(self):
        pass
