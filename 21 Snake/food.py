from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('white')
        self.speed('fastest')
        x_rand = random.randint(-280, 280)
        y_rand = random.randint(-280, 280)
        self.goto(x_rand, y_rand)
        self.refresh()

    def refresh(self):
        x_rand = random.randint(-280, 280)
        y_rand = random.randint(-280, 280)
        self.goto(x_rand, y_rand)
