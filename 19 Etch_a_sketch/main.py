from turtle import Turtle, Screen


def forward():
    tim.forward(10)


def left():
    tim.left(10)


def right():
    tim.right(10)


def back():
    tim.back(10)


tim = Turtle()
screen = Screen()
screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='a', fun=left)
screen.onkey(key='s', fun=back)
screen.onkey(key='d', fun=right)
screen.exitonclick()

