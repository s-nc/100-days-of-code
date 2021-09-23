from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5, 0.5)
        self.speed(8)
        self.color("purple")
        self.penup()
        initial_direction = [0, 0]
        while initial_direction[0] == 0 or initial_direction[1] == 0:
            initial_direction = [random.randint(-20, 20), random.randint(5, 20)]
        self.goto((0, -230))
        self.x_dir = initial_direction[0]
        self.y_dir = initial_direction[1]

    def move(self):
        self.goto(self.xcor() + self.x_dir, self.ycor() + self.y_dir)

    def reflect(self):
        self.x_dir = -self.x_dir

    def collide(self):
        self.y_dir = -self.y_dir

    def respawn(self):
        self.goto(0, -230)
        self.y_dir = -self.y_dir


