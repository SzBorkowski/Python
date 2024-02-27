import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.drive()

    # Detect crossing a finish line
    if player.ycor() > 280:
        player.start_line()
        scoreboard.made_it()
        #car_manager.faster()

    # Detect collision with a car
    if player.pos == car_manager.pos:
        game_is_on = False
        scoreboard.game_over()