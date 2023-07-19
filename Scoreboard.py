from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.player_score = 0
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.color("White")
        self.player_score_update()


    def player_score_count(self):
        self.player_score += 1
        self.clear()
        self.player_score_update()

    def player_score_update(self):
        self.write(arg=f" Score: {self.player_score}", move=False, align="Center", font=("Arial", 12, "bold"))

