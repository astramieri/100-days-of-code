import art
import data
import random
import os

def print_logo():
    os.system("cls")
    print(art.logo)

def get_random_entry():
    index = random.randint(0, len(data.list) - 1)
    return data.list.pop(index)

def has_more_followers(couple):
    if couple['A']['follower_count'] > couple['B']['follower_count']:
        return 'A'
    else:
        return 'B'

def print_challenge(couple):
    def format_entry(entry):
        return f"{entry['name']}, a {entry['description']}, from {entry['country']}."

    print(f"Compare A: {format_entry(couple['A'])}")
    print(art.vs)
    print(f"Against B: {format_entry(couple['B'])}")
    
def play_game():
    print_logo()

    is_game_over = False

    score = 0

    couple = {}
    
    couple["A"] = get_random_entry()
    couple["B"] = get_random_entry()

    while not is_game_over:
        print_challenge(couple)

        choice = input("Who has more followers? Type 'A' or 'B': ")

        print_logo()

        if choice == has_more_followers(couple):
            score += 1

            if len(data.list) != 0:
                print(f"You're right! Current score: {score}.")

                couple["A"] = couple[choice]
                couple["B"] = get_random_entry()
            else:
                print(f"You win! Final score: {score}.")
                is_game_over = True
        else:
            print(f"Sorry, that's wrong! Final score: {score}.")
            is_game_over = True

play_game()