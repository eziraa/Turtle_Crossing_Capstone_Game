import random
from turtle import Turtle

COLOR_LIST = ["red", "black", "green", "yellow", "orange", "pink"]


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLOR_LIST))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(5)

