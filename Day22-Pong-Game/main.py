# This is my pong game.

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle((370, 0))
paddle_2 = Paddle((-370, 0))
ball = Ball()
board = Scoreboard()

screen.listen()
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")

game_on = True
while game_on:
    ball.move()
    time.sleep(0.1)

    # Detect collisions with top and bottom wall and reflect
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.reflect()

    # Detect collisions with paddles
    if ball.xcor() >= 345 and paddle_1.distance(ball) <= 50:
        ball.bat()
    if ball.xcor() <= -345 and paddle_2.distance(ball) <= 50:
        ball.bat()

    # Detect paddle misses
    if ball.xcor() >= 380:
        board.left_scores()
        ball.respawn()
    if ball.xcor() <= -380:
        board.right_scores()
        ball.respawn()

    screen.update()

screen.exitonclick()
