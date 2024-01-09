from turtle import Turtle, Screen

turtle = Turtle()

screen = Screen()

def move_forwards():
    turtle.forward(10)

screen.listen()

# better using KEYWORD ARGUMENT
# no parentheses when passing the function name
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()