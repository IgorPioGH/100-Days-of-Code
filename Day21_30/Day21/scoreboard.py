from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)

    # game_over screen
    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write("GAME OVER",
                   align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=-30)
        self.write(f"Score: {self.score}",
                   align=ALIGNMENT, font=FONT)

    # refresh score
    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}",
                   align=ALIGNMENT, font=FONT)