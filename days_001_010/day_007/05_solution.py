import random
import hangman

print(f"{hangman.logo}")

chosen_word = random.choice(hangman.word_list)
secret_word = []
letters = []

def init():
    print(f"Chosen word: {chosen_word}\n")

    for letter in chosen_word:
        secret_word.append("_")

def play():
    game_over = False
    total_lives = 6 

    while not game_over:
        guess = input("Guess a letter: ").lower()

        if guess in letters:
            print(f"You already guessed '{guess}'\n")
        else:
            letters.append(guess)

            if guess in chosen_word:
                print(f"You guessed '{guess}', good job!")
                for i in range(len(chosen_word)):
                    if chosen_word[i] == guess:
                        secret_word[i] = guess
            else:
                print(f"You guessed '{guess}', that's not in the word. You lose a life.")
                total_lives -= 1
            
            print("")
            print(f"Secret word: {secret_word}")
            print(hangman.stages[total_lives])

            if not "_" in secret_word:
                game_over = True
                print("You win!")

            if total_lives == 0:
                game_over = True
                print("You lose.")

init()
play()



