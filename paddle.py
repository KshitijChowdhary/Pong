from turtle import Turtle

STARTING_POSITION = [(350, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len = 1, stretch_wid = 5)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)


    def down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)









