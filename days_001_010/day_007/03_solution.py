import random

word_list = ["apple", "banana", "orange", "coconut", "grape", "kiwi"] 

chosen_word = random.choice(word_list)

print(f"Chosen word: {chosen_word}")

secret_word = []

for letter in chosen_word:
    secret_word.append("_")

print(f"Secret word: {secret_word}")

game_over = False # initialization

while not game_over:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            secret_word[i] = guess

    print(f"Secret word: {secret_word}")

    if not "_" in secret_word:
        game_over = True
        print("You win!")

