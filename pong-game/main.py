from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(WIDTH, HEIGHT)
screen.title("Pong")
screen.tracer(0)

# Scoreboard
scoreboard = Scoreboard()

# create paddles and a ball
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()

# Key input
screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_deflect()

    if ball.distance(r_paddle) < 45 and ball.xcor() > 330 or ball.distance(l_paddle) < 45 and ball.xcor() < -330:
        ball.paddle_deflect()

    # Right miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    # Left miss
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
