from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")

screen = Screen()
screen.colormode(255)

turtle.teleport(200, 200)
turtle.dot(20, (255, 0, 0))
turtle.teleport(150, 200)
turtle.dot(20, (0, 255, 0))
turtle.teleport(100, 200)
turtle.dot(20, (0, 0, 255))



# angle = random.randrange(0, 360, 90)




for _ in range(10):
    turtle.setheading(0) # east
    
    for _ in range(10):
        pass
        # turtle.setheading()
        # angle = random.randrange(0, 360, 90)

        # print(angle)

        # r = random.randint(1, 255)
        # g = random.randint(1, 255)
        # b = random.randint(1, 255)

        # turtle.pencolor((r, g, b)) # a tuple is immutable

        # turtle.forward(30)
        # turtle.setheading(angle)

screen.exitonclick()