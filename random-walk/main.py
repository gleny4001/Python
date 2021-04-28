import turtle as t
import random
turtle = t.Turtle()
turtle.pensize(10)
directions = [0, 90, 180, 270]


t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb = (r,g,b)

    return rgb

while True:
    right_left = random.randint(0,1)
    turtle.forward(30)
    turtle.setheading(random.choice(directions))
    turtle.color(random_color())




