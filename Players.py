from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.pad = self.paddle(x, y)


    def paddle(self,x,y):

        piece1 = Turtle()
        piece1.shape("square")
        piece1.color("white")
        piece1.penup()
        piece1.speed(10)
        piece1.goto(x=x,y=y+20)

        piece2 = Turtle()
        piece2.shape("square")
        piece2.color("white")
        piece2.penup()
        piece2.speed("fastest")
        piece2.goto(x=x,y=y)

        piece3 = Turtle()
        piece3.shape("square")
        piece3.color("white")
        piece3.penup()
        piece3.speed("fastest")
        piece3.goto(x=x, y=y-20)

        list = [piece1, piece2, piece3]

        return list


    def paddle_move_up(self):
        if self.pad[0].ycor() < 381:
            for paddle_index in range(2, 0, -1):
                new_x = self.pad[paddle_index-1].xcor()
                new_y = self.pad[paddle_index-1].ycor()
                self.pad[paddle_index].goto(x=new_x, y=new_y)
            self.pad[0].setheading(90)
            self.pad[0].forward(distance=20)

    def paddle_move_down(self):

        if self.pad[2].ycor() > -380:

            for paddle_index in range(0, 2, 1):
                new_x = self.pad[paddle_index + 1].xcor()
                new_y = self.pad[paddle_index + 1].ycor()
                self.pad[paddle_index].goto(x=new_x, y=new_y)
            self.pad[2].setheading(270)
            self.pad[2].forward(distance=20)
