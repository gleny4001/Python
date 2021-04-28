from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter color: ").lower()
all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
winner_color = ""
is_race_on = False

def draw_line():
    """Draws the finishing line"""
    turtle = Turtle()
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(220,200)
    turtle.pendown()
    turtle.right(90)
    for i in range(20):
        turtle.forward(20)
        if i%2 == 0:
            turtle.penup()
        else:
            turtle.pendown()





def constructor(x, y, color):
    """Creates the turtle"""
    new_turtle = Turtle("turtle")
    new_turtle.speed(3)
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)


def move_turtle(num):
    """moves turtle in random speed and also check if the turtle crossed the line"""
    all_turtles[num].forward(random.uniform(0.0, 8.0))
    xcoordinate = int(all_turtles[num].xcor())
    #Check the winner
    if xcoordinate > 220:
        global winner_color
        global is_race_on
        winner_color = colors[num]
        is_race_on = False


draw_line()

#Creates 6 turtles
y = 140
for i in range(0, 6):
    constructor(-240, y, colors[i])
    y -= 50

if user_bet:
    is_race_on = True
while is_race_on:
    for i in range(0, 6):
        move_turtle(i)



#Final text for the user
if winner_color == user_bet:
    print(f"You win! {winner_color.capitalize()} won")

else:
    print(f"You lost. {winner_color.capitalize()} won")
