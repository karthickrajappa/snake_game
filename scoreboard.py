from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.current_score = 0
        with open("data.txt") as score:
            self.high_score = score.read()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Current score: {self.current_score} High score:{self.high_score}', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.current_score > int(self.high_score):
            self.high_score = self.current_score
            with open("data.txt", mode='w') as score:
                score.write(str(self.current_score))
            self.current_score = 0
            self.update_scoreboard()
