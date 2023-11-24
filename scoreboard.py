from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 65, 'normal')
POSITIONS = [(0,300), (0, 200), (0, 100), (0,0), (0,-300), (0, -200), (0, -100)]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, False, align = ALIGNMENT, font = FONT)
        self.goto(100, 200)
        self.write(self.r_score, False, align=ALIGNMENT, font=FONT)
        for position in POSITIONS:
            self.goto(position)
            self.write("|", False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()