# In this file, we create the Scoreboard object.
from turtle import Turtle

score_format = {"FONT": "Arial", "COLOUR": "pink", "SIZE": 16}


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.color(score_format["COLOUR"])
        self.penup()
        self.goto(310, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color(score_format["COLOUR"])
        self.write(f"Score: {self.score}\nLives: {self.lives}", align="center", font=(score_format["FONT"],
                                                                 score_format["SIZE"], "normal"))

    def scores(self, points):
        self.clear()
        self.score += points
        self.update_scoreboard()

    def lose_life(self):
        self.clear()
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto((0, -180))
        self.color("white")
        self.write("GAME OVER", align="center", font=(score_format["FONT"], 2*score_format["SIZE"], "normal"))

    def win(self):
        self.write("YOU WIN!", align="center", font=(score_format["FONT"], 2 * score_format["SIZE"], "normal"))

