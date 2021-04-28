from turtle import Turtle, Screen
import random



turtle = Turtle()
turtle.speed(0)
screen = Screen()

screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)



for i in range(45):
    turtle.circle(80)
    turtle.right(8)
    turtle.circle(80)
    turtle.color(random_color())

for i in range(45):
    turtle.circle(100)
    turtle.right(8)
    turtle.circle(100)
    turtle.color(random_color())

screen.exitonclick()



