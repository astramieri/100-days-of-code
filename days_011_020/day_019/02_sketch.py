# W = Forwards
# S = Backwards
# A = Counter-clockwise
# D = Clockwise
# C = Clear drawing

from turtle import Turtle, Screen


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_clockwise():
    turtle.right(10)


def turn_counter_clockwise():
    turtle.left(10)


def clean_drawing():
    # turtle.reset()
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown


turtle = Turtle()
screen = Screen()

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clean_drawing)

screen.exitonclick()
