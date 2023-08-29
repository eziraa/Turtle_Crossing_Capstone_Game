from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
is_game_on = True
while is_game_on:
    screen.update()