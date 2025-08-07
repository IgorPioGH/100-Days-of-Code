from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
aposta = screen.textinput(title="APOSTE NO GANHADOR!", prompt="Qual tartaruga irá vencer a corrida? Digite a cor: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False

if aposta:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == aposta:
                print(f"You win! The {winning_color} won the race.")
            else:
                print(f"You lose! The {winning_color} won the race.")
        rand_distance = random.randint(0,3)
        turtle.fd(rand_distance)

screen.exitonclick()