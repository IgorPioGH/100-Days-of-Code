from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(x=-270, y=250)
        self.write(f"{self.score}", font=FONT)

    def player_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", font=FONT, align="center")
        self.goto(x=0, y=-30)
        self.write(f"{self.score}", font=FONT, align="center")