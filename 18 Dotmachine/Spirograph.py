from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.shape('turtle')
tim.speed(0)
screen.colormode(255)
for _ in range(36):
    r = random.choice(range(255))
    g = random.choice(range(255))
    b = random.choice(range(255))
    tim.pencolor((r, g, b))
    tim.circle(100)
    tim.left(10)



screen.exitonclick()