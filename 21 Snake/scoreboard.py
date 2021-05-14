from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font="Arial, 25")

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font="Arial, 25")

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align='center', font="Arial, 25")
