from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("turtle")
        self.setheading(90)
        self.start_line()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def start_line(self):
        self.goto(STARTING_POSITION)