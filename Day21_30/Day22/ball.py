from turtle import Turtle
STEP_DISTANCE = 10
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x = 1
        self.y = 1
        self.move_speed = 0.1

    def move(self):
        self.goto(x=self.xcor() + STEP_DISTANCE * self.x, y=self.ycor() + STEP_DISTANCE * self.y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.7

    def restart(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
