from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 10, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.penup()
        self.color("white")
        self.goto(0, +270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update()
