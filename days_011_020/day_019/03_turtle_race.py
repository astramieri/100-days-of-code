from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "gray", "green", "blue", "orange", "purple"]

x = -200
y = +140

for color in colors:
    y -= 40
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(x=x, y=y)

screen.exitonclick()