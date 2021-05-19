from turtle import Turtle

shape = 'circle'
color = 'white'
start_dir = 40


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape(shape)
        self.setheading(start_dir)
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_reflect(self):
        self.y_move *= -1

    def bounce(self):
        self.x_move *= -1

    def speed_increase(self):
        if self.y_move < 0:
            self.y_move -= .1
        elif self.y_move > 0:
            self.y_move += .1
        if self.x_move < 0:
            self.x_move -= .1
        elif self.x_move > 0:
            self.x_move += .1




