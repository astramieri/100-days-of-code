# Scope

enemies = 1

def increase_enemies_1():
    global enemies # error prone (AVOID MODIFYNG GLOBAL VARIABLES!)
    enemies += 1
    return enemies

def increase_enemies_2():
    return enemies + 1 # better approach

print(increase_enemies_1())
print(increase_enemies_2())

