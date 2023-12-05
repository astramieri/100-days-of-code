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

while not at_goal():
    if front_is_clear():
        move()
        
        if not wall_on_right():
            turn_right()
    else:
        turn_right()  
    
    