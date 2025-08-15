from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
# Variables
# Create Scren
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
# need to make moviment fluid
screen.tracer(0)
# create the paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
# need to control paddles with keyboard
screen.listen()

#ball
ball = Ball()

#score
r_score = Score((100, 200))
l_score = Score((-100, 200))

is_game_on = True
while is_game_on:
    # Make the moviment more fluid
    screen.update()
    # Ball speed
    time.sleep(ball.move_speed)
    # Control left paddle
    screen.onkeypress(l_paddle.move_up, "w")
    screen.onkeypress(l_paddle.move_down, "s")

    # Control right paddle
    screen.onkeypress(r_paddle.move_up, "Up")
    screen.onkeypress(r_paddle.move_down, "Down")
    # move ball
    ball.move()
    # Detect the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # R paddle miss
    if ball.xcor() > 380:
        ball.restart()
        l_score.score += 1
        l_score.update_score()

    # L paddle miss
    if ball.xcor() < - 380:
        ball.restart()
        r_score.score += 1
        r_score.update_score()

screen.exitonclick()