from turtle import Turtle

STARTING_POSITION = (0, -280)
DISTANCE_MOVE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.score = 0
        self.turtle = Turtle("turtle")
        self.turtle.shapesize(stretch_len=1, stretch_wid=2)
        self.turtle.color("green")
        self.turtle.penup()
        self.turtle.setheading(90)
        self.turtle.goto(STARTING_POSITION)

    def move(self):
        self.turtle.forward(DISTANCE_MOVE)

    def reset(self):
        self.turtle.goto(STARTING_POSITION)
