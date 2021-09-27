# File to create functionality of blocks.
from turtle import Turtle


class Block(Turtle):
    def __init__(self, co_ord, colour):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.75, stretch_len=2.5)
        self.color(colour)
        self.color_string = colour
        self.speed("fastest")
        self.penup()
        self.goto(co_ord)

    def disappear(self):
        self.hideturtle()

