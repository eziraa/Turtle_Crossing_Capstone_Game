import random
from turtle import Turtle, Screen
from player import FINISH_LINE_Y
from score_board import ScoreBoard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
number_of_car = random.randint(14, 17)
car_manager = CarManager()
score_board = ScoreBoard()
screen.onkey(score_board.player.move, "Up")
is_game_on = True
while is_game_on:
    time.sleep(0.1)

    screen.update()
    car_manager.create_cars()
    car_manager.move()

    # Detect collision between the turtle and the upper wall
    if score_board.player.turtle.ycor() > FINISH_LINE_Y:
        score_board.update_score()
        score_board.player.reset()
    # Detect collision between the turtle and the car
    for car in car_manager.all_cars:
        if car.distance(score_board.player.turtle) < 30 and abs(car.ycor() - score_board.player.turtle.ycor()) < 10:
            score_board.game_over()
            is_game_on = False

screen.exitonclick()
