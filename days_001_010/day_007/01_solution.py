import random

word_list = ["apple", "banana", "orange", "coconut", "grape", "kiwi"] 

chosen_word = random.choice(word_list)

print(f"Chosen word: {chosen_word}")

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right!")
    else:
        print("Wrong.")