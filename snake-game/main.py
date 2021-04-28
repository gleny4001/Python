from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score

# Screen setup (screen size, background color, title)
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detecting food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        snake.reset()
        score.reset()



    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            snake.reset()
            score.reset()






screen.exitonclick()
