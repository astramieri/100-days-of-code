def move():
    pass

def turn_left():
    pass

def at_goal():
    pass

def wall_in_front():
    pass

def wall_on_right():
    pass

def front_is_clear():
    pass

def right_is_clear():
    pass

# solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not wall_in_front():
    move()

while not wall_on_right():
    turn_left()

while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        move()
    
    