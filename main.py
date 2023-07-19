import time
import random
from ball import  Ball
from turtle import Screen
from Players import Paddle
from Scoreboard import Scoreboard

window = Screen()
window.bgcolor("black")
window.setup(width=1000,height=805)
window.title(titlestring="PingPong")
window.listen()
window.tracer(0)

game_on = True
player1 = Paddle(x=-480,y=0)
player_1 = player1.pad
player2 = Paddle(x=480,y=0)
player_2 = player2.pad
ball = Ball()
ball.ball_launch()
player1_score = Scoreboard(x=-250,y=380)
player2_score = Scoreboard(x=250,y=380)


while game_on:
    window.update()
    time.sleep(0.05)
    ball.move()
    window.onkeypress(key="Up", fun=player2.paddle_move_up)
    window.onkeypress(key="Down", fun=player2.paddle_move_down)
    window.onkeypress(key="w", fun=player1.paddle_move_up)
    window.onkeypress(key="s", fun=player1.paddle_move_down)

    if ball.ycor() >= 390:
        if 0 < ball.heading() < 90:
            ball.setheading(random.randint(280, 350))
        elif 90 < ball.heading() < 180:
            ball.setheading(random.randint(190, 260))

    if ball.ycor() <= -390:
        if 270 < ball.heading() < 360:
            ball.setheading(random.randint(10, 80))
        elif 180 < ball.heading() < 270:
            ball.setheading(random.randint(100, 170))

    if ball.distance(player_1[0]) < 25:
        ball.setheading(random.randint(10,80))
    elif ball.distance(player_1[1]) < 25:
        ball.setheading(random.randint(-10, 10))
    elif ball.distance(player_1[2]) < 25:
        ball.setheading(random.randint(280, 350))

    if ball.distance(player_2[0]) < 25:
        ball.setheading(random.randint(100,170))
    elif ball.distance(player_2[1]) < 25:
        ball.setheading(random.randint(170,190))
    elif ball.distance(player_2[2]) < 25:
        ball.setheading(random.randint(190, 260))

    if ball.xcor() < -500:
        player2_score.player_score_count()
        ball.goto(x=0,y=0)
        for piece in player_1:
            piece.clear()
        for piece in player_2:
            piece.clear()
        ball.ball_launch()


    if ball.xcor() > 500:
        player1_score.player_score_count()
        ball.goto(x=0,y=0)
        for piece in player_1:
            piece.clear()
        for piece in player_2:
            piece.clear()
        ball.ball_launch()






window.exitonclick()
