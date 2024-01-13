from turtle import Turtle

DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self, tail=3):
        self.segments = []
        self.create(tail)
        self.head = self.segments[0]

    def create(self, tail):
        x = 0
        y = 0

        for i in range(0, tail):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(x=i*(-20), y=0)

            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)

        self.segments[0].forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
