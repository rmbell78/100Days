import colorgram
from turtle import Turtle, Screen
import random


def rgb_gen():
    rgb_list = []
    colors = colorgram.extract('Hirstdot.jpg', 30)
    for color in colors:
        rgb = [color.rgb.r, color.rgb.g, color.rgb.b]
        rgb_list.append(rgb)
    return rgb_list


def tim_move():
    pos = tim.pos()
    if pos[0] > 290:
        tim.goto(-300, (pos[1] - 75))
    else:
        tim.goto((pos[0] + 100), pos[1])


def clr_draw(rgb):
    sel = random.choice(range(29))
    tim.dot(50, rgb_list[sel])


tim = Turtle()
screen = Screen()
tim.shape('turtle')
tim.penup()
tim.goto(-300, 250)
tim.speed(7)
screen.colormode(255)
rgb_list = rgb_gen()
for _ in range(56):
    clr_draw(rgb_list)
    tim_move()

screen.exitonclick()
