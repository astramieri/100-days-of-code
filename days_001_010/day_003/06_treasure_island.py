print('''
##############################
# Welcome to Treasure Island #
##############################
''')
print("Your mission is to find the treasure.")

choice1 = input("You're at a cross road. Where do you want to go? Left or Right? ")

if choice1.lower() == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Wait or Swim? ")

    if choice2.lower() == "wait":
        choice3 = input("You arrived at the insland unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colouur do you choose? ")
        
        if choice3.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3.lower() == "blue":
            print("It's a room full of water. Game Over.")  
        else:
            print("You found the treasure! You Win!")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
