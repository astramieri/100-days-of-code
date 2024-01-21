from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # turn off animation

paddle = Paddle()

screen.listen()
screen.onkey(paddle.up, "Up")       # do not use parantheses!
screen.onkey(paddle.down, "Down")   # do not use parantheses!

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()