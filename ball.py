import random
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.45, stretch_len=0.45)
        self.speed(1)


    def move(self):
        self.forward(20)


    def ball_launch(self):
        if self.xcor() == 0 and self.ycor() == 0:
            self.setheading(random.randint(135, 225))
