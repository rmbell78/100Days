from snake import Snake
from turtle import Screen
import food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake = Snake()
screen.update()

food = food.Food()
score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key='w')
screen.onkey(fun=snake.left, key='a')
screen.onkey(fun=snake.down, key='s')
screen.onkey(fun=snake.right, key='d')

game_on = True
while game_on:
    snake.move()
    screen.update()
    # food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.increase()

    # wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_on = False

    # Tail Collision
    for segment in snake.snake_seg[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_on = False


screen.exitonclick()
