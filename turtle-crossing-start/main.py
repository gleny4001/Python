import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Scoreboard
scoreboard = Scoreboard()

# Player
player = Player()

# car_manager
num_of_cars = 10
move_speed = 0.1
cars = [CarManager() for i in range(num_of_cars)]

screen.onkey(player.up, "Up")

# Game loop
game_is_on = True

while game_is_on:
    time.sleep(move_speed)
    # Next level
    if player.ycor() > 280:
        player.reset()
        scoreboard.level_up()
        move_speed *= 0.8
        # Add more cars
        for i in range(0, 2):
            cars.append(CarManager())

    # Car regeneration
    for car in cars:
        car.move()
        if car.xcor() < -300:
            car.reset()
        if player.distance(car.xcor(), car.ycor()) < 23:
            game_is_on = False
            scoreboard.game_over()

    screen.update()

screen.exitonclick()
