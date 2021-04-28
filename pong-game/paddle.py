from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.left(90)
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.penup()
        self.goto(x_cor, y_cor)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
