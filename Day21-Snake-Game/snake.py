# In this file, we create the snake class.
from turtle import Turtle
fwd_distance = 20
directions = {"up": 90, "down": 270, "left": 180, "right": 0}


class Snake:
    def __init__(self, snake_len):
        self.start_length = snake_len
        self.snake = []
        self.spawn_snake(self.start_length)
        self.head = self.snake[0]
        self.length = len(self.snake)

    def spawn_snake(self, snake_len):
        # creating snake of specified length
        initial_position = []
        for i in range(snake_len):
            initial_position.append((-20 * i, 0))
        for co_ord in initial_position:
            self.add_segment(co_ord)

    def add_segment(self, co_ord):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(co_ord)
        self.snake.append(segment)

    def grow(self):
        self.add_segment(self.snake[-1].position())
        self.length += 1

    def move(self):
        for tail in range(1, self.length):
                self.snake[-tail].goto(self.snake[-tail - 1].position())
        self.head.forward(fwd_distance)

    def up(self):
        if self.head.heading() != directions["down"]:
            self.head.setheading(directions["up"])

    def down(self):
        if self.head.heading() != directions["up"]:
            self.head.setheading(directions["down"])

    def left(self):
        if self.head.heading() != directions["right"]:
            self.head.setheading(directions["left"])

    def right(self):
        if self.head.heading() != directions["left"]:
            self.head.setheading(directions["right"])

    def reset(self):
        for i in range(self.length):
            self.snake[i].goto((1000, 1000))
        self.snake = []
        self.spawn_snake(self.start_length)
        self.length = self.start_length
        self.head = self.snake[0]
