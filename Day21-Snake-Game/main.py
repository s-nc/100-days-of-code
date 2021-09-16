from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake(3)
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    # Detect collision with wall
    if snake.head.xcor() > screen.window_width()/2 - 20 or snake.head.xcor() < 20 - screen.window_width()/2 \
            or snake.head.ycor() > screen.window_width()/2 - 20 or snake.head.ycor() < 20 - screen.window_width()/2:
        snake.reset()
        scoreboard.reset()

    # Detect collision with tail
    for i in range(1, snake.length):
        if snake.head.distance(snake.snake[i]) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
