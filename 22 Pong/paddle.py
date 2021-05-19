from turtle import Turtle

start_y = 0
shape = 'square'
color = 'white'
speed = 0
stretch_x = 5
stretch_y = 1


class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        if player == 'cpu':
            start_x = 350
        elif player == 'player':
            start_x = -350
        self.penup()
        self.speed(speed)
        self.color(color)
        self.shape(shape)
        self.shapesize(stretch_wid=stretch_x, stretch_len=stretch_y)
        self.setpos(start_x, start_y)

    def up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)



