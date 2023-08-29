from turtle import Turtle
from player import Player

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.penup()
        self.color("black")
        self.goto(-270, 250)
        self.write(f"Level: {self.player.level}", align="left", font=FONT)
        self.hideturtle()

    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write("GAME  OVER!!!", align="center",  font=FONT)

    def update_score(self):
        self.clear()
        self.player.score += 10
        self.goto(0, 270)
        self.write(f"Score: {self.player.score}", align="center", font=FONT)

