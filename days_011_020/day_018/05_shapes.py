from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")

screen = Screen()
screen.colormode(255)

for edge in range(3,11):
    angle = 360 / edge

    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    turtle.pencolor((r, g, b))

    for _ in range(edge):
        turtle.forward(100)
        turtle.right(angle)


screen.exitonclick()