# Tic-Tac-Toe Board Game

class Board:
    def __init__(self):
        self.top = ["___", "___", "___"]
        self.middle = ["___", "___", "___"]
        self.bottom = ["___", "___", "___"]
        self.board = self.top[0]+"|"+self.top[1]+"|"+self.top[2] +"\n" +\
                     self.middle[0] + "|" + self.middle[1] + "|" + self.top[2] + "\n" +\
                     self.bottom[0] + "|" + self.bottom[1] + "|" + self.bottom[2]

    def update(self):
        self.board = self.top[0] + "|" + self.top[1] + "|" + self.top[2] + "\n" + \
                     self.middle[0] + "|" + self.middle[1] + "|" + self.middle[2] + "\n" + \
                     self.bottom[0] + "|" + self.bottom[1] + "|" + self.bottom[2]

    def check_for_winner(self):
        winner = False
        # check rows
        for row in [self.top, self.middle, self.bottom]:
            if (row[0] != "___") and (row[0] == row[1]) and (row[1] == row[2]):
                winner = True
        # check columns
        for col in [0, 1, 2]:
            if (self.top[col] != "___") and (self.top[col] == self.middle[col]) and (self.middle[col] == self.bottom[col]):
                winner = True
        # checking diagonals
        if self.middle[1] != "___":
            if (self.top[0] == self.middle[1]) and (self.middle[1] == self.bottom[2]):
                winner = True
            elif (self.top[2] == self.middle[1]) and (self.middle[1] == self.bottom[0]):
                winner = True
        return winner