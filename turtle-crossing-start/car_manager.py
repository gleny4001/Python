import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.penup()
        self.shapesize(1, 2)
        self.color(COLORS[random.randint(0, 5)])
        self.goto(random.randint(-280, 280), random.randint(-250, 240))

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def reset(self):
        self.goto(320, random.randint(-250, 240))
