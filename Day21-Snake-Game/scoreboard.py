# In this file, we create the Scoreboard object.
from turtle import Turtle
score_format = {"ALIGNMENT": "center", "FONT": "Arial", "COLOUR": "blue", "SIZE": 18}

with open("data.txt") as storage:
    all_time_high = int(storage.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = all_time_high
        self.color(score_format["COLOUR"])
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=score_format["ALIGNMENT"],
                   font=(score_format["FONT"], score_format["SIZE"], "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as storage:
                storage.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    """def game_over(self):
        self.goto((0,0))
        self.color("white")
        self.write("GAME OVER", align=score_format["ALIGNMENT"])"""



