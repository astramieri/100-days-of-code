
import random

special = ["#", "@", "!", "?", "*", "^"]

print("Welcome to the password generator!")

letters = int(input("How many letters would you like in your password? "))

symbols = int(input("How many symbols would you like? "))

numbers = int(input("How many numbers would you like? "))

password = []

for i in range(0, letters):
    number = random.randint(ord("a"), ord("z")) ## ascii table 
    letter = chr(number)
    
    case = random.randint(1, 2)
    if case % 2 == 0:
        letter = letter.upper()

    password.append(letter)

for i in range(0, symbols):
    index = random.randint(0, len(special)-1)
    password.append(special[index])

for i in range(0, numbers):
    letter = str(random.randint(0, 10))
    password.append(letter)

print(password)

random.shuffle(password)

print(password)

password_string = ""

for i in range(0, len(password)):
    password_string += password[i]

print(f"Password generated: {password_string}")