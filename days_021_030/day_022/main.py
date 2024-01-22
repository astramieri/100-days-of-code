from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # turn off animation

r_paddle = Paddle((+350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

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

    # dectect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collisio with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > +320:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()