from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 255)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"score: {self.score} High score : {self.highscore}", move=False, align=ALIGNMENT,
                       font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER!", move=False, align=ALIGNMENT, font=FONT)
    #     self.goto(0, -30)
    #     self.write(arg=f"Final score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
