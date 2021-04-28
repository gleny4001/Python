from turtle import Turtle
import random

COLORS = ["red","orange","yellow","green","blue","indigo","purple"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color(COLORS[random.randint(0,len(COLORS)-1)])
        self.speed(0)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color(COLORS[random.randint(0,len(COLORS) - 1)])
        self.goto(random_x, random_y)

    def reset_food(self):
        self.reset()
