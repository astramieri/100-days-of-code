from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("purple")

for _ in range(4):
    for _ in range(5):
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
    turtle.right(90)

screen = Screen()
screen.exitonclick()