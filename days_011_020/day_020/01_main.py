from turtle import Screen
from snake import Snake
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True

while game_is_on:
    time.sleep(0.3)
    screen.update()
    snake.move()
        
screen.exitonclick()


    