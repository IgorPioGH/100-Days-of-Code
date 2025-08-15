from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
class Score(Turtle):
    def __init__(self, position):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.score = 0
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(self.score, align=ALIGNMENT, font=FONT)
