# Number Guessing Game

import random

answer = random.randint(1, 100)

attempts = 0

is_game_over = False  

def make_a_guess():
    global attempts
    global is_game_over

    print(f"You have {attempts} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    if guess == answer:
        print(f"You win! 😎")
        is_game_over = True
    elif guess < answer:
        print(f"Too low! 😤")
        attempts -= 1
    elif guess > answer:
        print(f"Too high! 😤")
        attempts -= 1

    if attempts == 0:
        print(f"You lose! 😭")
        is_game_over = True

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

while not is_game_over:
    make_a_guess()