from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# a turtle has a dimension of 20x20

x = 0
y = 0

segments = []

for i in range(0, 3):
    turtle = Turtle()
    turtle.shape("square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(x=i*(-20), y=0)
    segments.append(turtle)

screen.update()

game_is_on = True
while game_is_on:

    time.sleep(0.5)
    screen.update()

    for i in range(len(segments) - 1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    segments[0].forward(20)
    segments[0].right(90)
        
screen.exitonclick()


    