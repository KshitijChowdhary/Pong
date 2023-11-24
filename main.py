from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

#Screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

#Control
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.hit()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit()

    #Detect when paddle misses ball
    #Right side misses
    if ball.distance(r_paddle) > 50 and ball.xcor() > 380:
        ball.miss()
        scoreboard.l_point()

    #Left side misses
    if ball.distance(l_paddle) > 50 and ball.xcor() < -380:
        ball.miss()
        scoreboard.r_point()







screen.exitonclick()
