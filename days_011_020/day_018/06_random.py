from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.speed("fast")
turtle.pensize(20)

screen = Screen()
screen.colormode(255)

for _ in range(100):
    angle = random.randrange(0, 360, 90)

    print(angle)

    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    turtle.pencolor(r, g, b)

    turtle.forward(30)
    turtle.setheading(angle)

screen.exitonclick()