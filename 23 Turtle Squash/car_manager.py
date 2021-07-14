import turtle
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []

    def random_start(self):
        if random.choice([0, 1, 2, 3, 4]) == 1:
            ncar = Turtle()
            ncar.penup()
            ncar.setpos(300, random.choice(range(-240, 240, 20)))
            ncar.color(random.choice(COLORS))
            ncar.shape('square')
            ncar.shapesize(stretch_len=3)
            self.cars.append(ncar)

    def move(self):
        for i in self.cars:
            i.back(STARTING_MOVE_DISTANCE)
