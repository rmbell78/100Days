from turtle import Turtle
import time

Up = 90
Right = 0
Down = 270
Left = 180


class Snake:
    def __init__(self):
        self.snake_seg = []
        self.start()
        self.head = self.snake_seg[0]

    def move(self):
        time.sleep(.1)
        for seg_num in range(len(self.snake_seg) - 1, 0, -1):
            go_to_cor = (self.snake_seg[seg_num - 1].xcor(), self.snake_seg[seg_num - 1].ycor())
            self.snake_seg[seg_num].goto(go_to_cor)
        self.snake_seg[0].forward(20)

    def start(self):
        start_x = [0, -20, -40]
        count = 0
        for _ in range(3):
            snake = Turtle()
            snake.penup()
            snake.shape('square')
            snake.color('white')
            snake.goto(x=start_x[count], y=0)
            count += 1
            self.snake_seg.append(snake)

    def increase(self):
        snake = Turtle()
        snake.penup()
        snake.shape('square')
        snake.color('white')
        self.snake_seg.append(snake)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)
