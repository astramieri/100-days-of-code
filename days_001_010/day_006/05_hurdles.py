def move():
    pass

def turn_left():
    pass

def at_goal():
    pass

def wall_in_front():
    pass

def front_is_clear():
    pass

## solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()