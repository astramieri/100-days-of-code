from turtle import Turtle, Screen
import random

WIDTH=500
HEIGHT=400

is_race_on = False

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "gray", "green", "blue", "orange", "purple", "brown", "white", "gold"]

x = -200
y = +140

turtles = []

for i in range(0, 5):
    y -= 40

    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=x, y=y)

    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() > (WIDTH / 2 -20):
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

            is_race_on = False
            
            break

screen.exitonclick()