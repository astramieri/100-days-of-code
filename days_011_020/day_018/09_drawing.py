from turtle import Turtle, Screen
import random
import colorgram

color_list = []

def extract_colors():
    colors = colorgram.extract('./days_011_020/day_018/hirst.webp', 10)

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        color_list.append((r, g, b))

def draw_dots():
    turtle = Turtle()
    turtle.shape("triangle")
    turtle.speed("slowest")

    screen = Screen()
    screen.colormode(255)   

    x = -250
    y = -250

    direction = -1

    SIZE = 20
    
    DIMENSION = 10

    for row in range(DIMENSION):
        y += 50

        direction *= -1

        for col in range(DIMENSION):
            if col == 0:
                pass
            else:
                x += 50 * (direction) 
            
            color = random.choice(color_list)
            
            turtle.teleport(x, y)
            turtle.dot(SIZE, color)
            

    screen.exitonclick()





# turtle.teleport(200, 200)
# 
# turtle.teleport(150, 200)
# turtle.dot(20, (0, 255, 0))
# turtle.teleport(100, 200)
# turtle.dot(20, (0, 0, 255))




# angle = random.randrange(0, 360, 90)

extract_colors()
draw_dots()






#         # print(angle)

#         # r = random.randint(1, 255)
#         # g = random.randint(1, 255)
#         # b = random.randint(1, 255)

#         # turtle.pencolor((r, g, b)) # a tuple is immutable

#         # turtle.forward(30)
#         # turtle.setheading(angle)

# 