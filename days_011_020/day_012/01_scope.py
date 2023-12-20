# Scope

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside fuction: {enemies}")

increase_enemies()
print(f"enemies inside fuction: {enemies}")

# Global Scope
player_health = 10

# Local Scope
def game():
    def drink_potion():
        potion_strength = 2
        print(potion_strength)
        print(player_health)

    drink_potion()

game()
# print(potion_strength) # this raises a NameErro


if True:
    my_variable = 2

print(my_variable) # there is no block scope!
