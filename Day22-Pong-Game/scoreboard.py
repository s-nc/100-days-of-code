# In this file, we create the Scoreboard object.
from turtle import Turtle

score_format = {"FONT": "Arial", "COLOUR": "pink", "SIZE": 16}


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.color(score_format["COLOUR"])
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score_1}     ", align="right", font=(score_format["FONT"],
                                                                 score_format["SIZE"], "normal"))
        self.write(f"     Score: {self.score_2}", align="left", font=(score_format["FONT"],
                                                                  score_format["SIZE"], "normal"))

    def left_scores(self):
        self.clear()
        self.score_1 += 1
        self.update_scoreboard()

    def right_scores(self):
        self.clear()
        self.score_2 += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto((0, 0))
        self.color("white")
        self.write("GAME OVER", align=score_format["ALIGNMENT"])
