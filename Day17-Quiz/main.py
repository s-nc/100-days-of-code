from turtle import Turtle, Screen

timmy = Turtle()

"""

Note: this is really day 18
timmy.forward(150)
timmy.left(90)
timmy.forward(150)
timmy.left(90)
timmy.forward(150)
timmy.left(90)
timmy.forward(150)
timmy.left(90)
"""

for i in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


screen = Screen()
screen.exitonclick()
