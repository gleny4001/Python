import colorgram
from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.hideturtle()
screen = Screen()
screen.colormode(255)
screen.screensize(100,100)
rgb_colors =[]
colors = colorgram.extract("image.jpg", 100)
turtle.speed(0)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

x = -250
y = 250
turtle.penup()
turtle.setposition(x, y)


for i in range(10):
    for j in range(10):
        turtle.dot(20, random.choice(rgb_colors))
        turtle.forward(50)
    y -= 50
    turtle.setposition(x, y)




screen.exitonclick()


