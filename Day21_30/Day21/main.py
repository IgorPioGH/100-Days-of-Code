from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)


# Crates snake
snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "d")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.level_up()
        scoreboard.score += 1
        scoreboard.refresh()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -299 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("Game Over! You hit the wall.")
        print(f"You scored: {scoreboard.score}")
        scoreboard.game_over()
        is_game_on = False

    # Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_on = False





screen.exitonclick()