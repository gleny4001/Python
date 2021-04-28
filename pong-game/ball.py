from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_speed = 10
        self.y_speed = 10
        self.move_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_speed
        y_cor = self.ycor() + self.y_speed
        self.goto(x_cor, y_cor)

    def wall_deflect(self):
        self.y_speed *= -1

    def paddle_deflect(self):
        self.x_speed *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.paddle_deflect()
