from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5) # Divide o padrao 20x20 por 2 -> 10x10
        self.color("red")
        self.speed("fastest") # faz com que a comida apareca ja no lugar, sem animaçao de ir ate la
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-280, 280),
                  y=random.randint(-280, 280))  # posiciona a comida em lugares aleatorios, evitando as bordas