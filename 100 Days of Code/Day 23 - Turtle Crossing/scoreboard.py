from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.color("black")
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def made_it(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", fony=FONT)
