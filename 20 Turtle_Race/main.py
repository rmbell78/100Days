from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=800, height=800)
colors = ["red", 'blue', 'green', 'orange', 'purple', 'violet']


def turtle_gen():
    turtle_dict = {}
    for i in colors:
        x = i
        i = Turtle()
        i.shape('turtle')
        i.color(x)
        i.penup()
        turtle_dict[x] = i
    return turtle_dict


def lineup(turtle_dict):
    contestants = len(turtle_dict)
    separation = 200 / contestants
    y = (-100)
    count = 0
    for i in turtle_dict.values():
        i.goto(-350, y)
        y = y + separation


def race(turtle_dict):
    for i in turtle_dict.values():
        i.forward(random.choice(range(30)))
        if i.xcor() > 300:
            key = [key for key in turtle_dict.items() if key[1] == i][0][0]
            return key
    return 0


def main():
    p_choice = screen.textinput(title='Choose A Racer', prompt=colors).lower()
    winner = 0
    t_dict = turtle_gen()
    lineup(t_dict)
    while winner == 0:
        winner = race(t_dict)
    if winner == p_choice:
        print('You won!')
    else:
        print('Sorry, the winner was ' + str(winner))


main()
screen.exitonclick()
