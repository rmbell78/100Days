from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

player = Paddle('player')
cpu = Paddle('cpu')
ball = Ball()
score = Scoreboard()
screen.update()

screen.listen()
screen.onkey(key='w', fun=player.up)
screen.onkey(key='s', fun=player.down)
screen.onkey(key='o', fun=cpu.up)
screen.onkey(key='l', fun=cpu.down)


game_on = True

while game_on:

    screen.listen()
    screen.onkey(key='w', fun=player.up)
    screen.onkey(key='s', fun=player.down)
    screen.onkey(key='o', fun=cpu.up)
    screen.onkey(key='l', fun=cpu.down)

    screen.update()
    ball.move()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.wall_reflect()

    if ball.xcor() > 340 or ball.xcor() < -340:
        if ball.distance(player) < 50 or ball.distance(cpu) < 50:
            ball.bounce()
            score.increase()
            ball.speed_increase()

    if ball.xcor() > 400 or ball.xcor() < -400:
        score.game_over()


screen.exitonclick()