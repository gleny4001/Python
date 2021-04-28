import turtle
import pandas

# Screen setup
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(725, 491)
turtle.shape(image)
FONT = ("Comic Sans MS", 10, "normal")

# pandas setup
df = pandas.read_csv("50_states.csv")

# Write on screen setup
write_state = turtle.Turtle()
write_state.hideturtle()
write_state.penup()

# Score setup
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
correct_guesses = 0


def write_on_screen(state, x, y):
    """write on the screen"""
    write_state.goto(x, y)
    write_state.write(f"{state}", align="center", font=FONT)


def score():
    """Write the score on the screen : n/50"""
    scoreboard.clear()
    scoreboard.goto(300, -150)
    scoreboard.write(f"{correct_guesses}/50", align="center", font=("Comic Sans MS", 20, "normal"))


guessed_states = []
while True:
    score()
    if correct_guesses == 50:
        print("Wow you've guessed all the states!")
        break
    # Ask user's guess on popup and title it to match with dataframe
    user_answer = str(screen.textinput(title="Guess the state", prompt="Name a state")).title()
    # Find the guess on csv file, and store it
    user_state = df[df.state == user_answer]
    if not user_state.empty:
        write_on_screen(user_state.state.item(), user_state.x.item(), user_state.y.item())
        guessed_states.append(user_state.state.item())
        correct_guesses += 1
    elif user_answer == "Quit":
        break
    else:
        pass

# Create new csv file taht contains the states that user did not guess
exclude = df.state.isin(guessed_states)
df[~exclude].state.to_csv("states_to_learn.csv")
