from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.speed("fast")
turtle.pensize(10)

screen = Screen()
screen.colormode(255)

for _ in range(100):
    angle = random.randrange(0, 360, 90)

    print(angle)

    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    turtle.pencolor((r, g, b)) # a tuple is immutable

    turtle.forward(30)
    turtle.setheading(angle)

screen.exitonclick()