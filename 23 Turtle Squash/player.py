from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
START_HEADING = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.setpos(STARTING_POSITION)
        self.setheading(START_HEADING)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)