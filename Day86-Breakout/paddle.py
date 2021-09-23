# File to create functionality of paddle.
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, co_ord):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(co_ord)

    def move_left(self):
        if self.xcor() >= -390 + self.shapesize()[1]*10:
            self.goto(self.xcor() - 20, self.ycor())

    def move_right(self):
        if self.xcor() <= 390 - self.shapesize()[1]*10:
            self.goto(self.xcor() + 20, self.ycor())

