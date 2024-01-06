from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.speed("fastest")
#turtle.pensize(10)

screen = Screen()
screen.colormode(255)

for i in range(1, 100):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    turtle.pencolor((r, g, b)) # a tuple is immutable

    new_heading = random.choice([-1, 1]) * 10

    turtle.setheading(turtle.heading() + new_heading)

    turtle.circle(50)
    

screen.exitonclick()