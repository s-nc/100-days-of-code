# This is my breakout game.

from turtle import Screen
from block import Block
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# -------------------- GAME SCREEN SETUP -------------------- #
screen = Screen()
screen.bgcolor("black")
screen.setup(width=780, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -250))

ball = Ball()
board = Scoreboard()

# Create wall of blocks.
colours = ["yellow", "yellow", "green", "green", "orange", "orange", "red", "red"]
points = {"yellow": 1, "green": 3, "orange": 5, "red": 7}
wall = []
for i in range(8*14):
    wall.append(Block((355 - 55*(i // 8), 20*(i % 8)), colours[i % 8]))

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

# -------------------- GAME PLAY -------------------- #
game_on = True
while game_on:
    ball.move()
    time.sleep(0.1)

    # Detect collisions with side walls and reflect.
    if ball.xcor() >= 380 or ball.xcor() <= -380:
        ball.reflect()

    # Detect collisions with blocks and remove block.
    for block in wall:
        if abs(ball.xcor() - block.xcor()) <= block.shapesize()[1]*10+5:
            if abs(ball.ycor() - block.ycor()) <= block.shapesize()[0]*10+5:
                wall.remove(block)
                block.disappear()
                ball.collide()
                board.scores(points[block.color_string])
                if block.color_string == "red":
                    paddle.shapesize(stretch_len=1.25)
                    paddle.speed("fastest")
                break

    # Detect collisions with paddle.
    if abs(ball.xcor() - paddle.xcor()) <= paddle.shapesize()[1]*10+7:
        if abs(ball.ycor() - paddle.ycor()) <= paddle.shapesize()[0]*10+7:
            ball.collide()

    # Detect paddle misses.
    if ball.ycor() <= -290:
        board.lose_life()
        ball.respawn()

    # Game over if you hit floor 3 times.
    if board.lives <= 0:
        board.game_over()
        game_on = False

    # Detect completion of blocks.
    if len(wall) == 0:
        board.win()
        game_on = False

    screen.update()

screen.exitonclick()
