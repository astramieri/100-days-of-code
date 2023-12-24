import art
import data
import random

score = 0

print(art.logo)

def get_random_entry():
    index = random.randint(0, len(data.list) - 1)
    return data.list.pop(index)

def print_entry(entry, text):
    print(f"{text} A: {entry['name']}, a {entry['description']}, from {entry['country']}.")

def has_more_followers(couple):
    if couple['A']['follower_count'] > couple['B']['follower_count']:
        return 'A'
    else:
        return 'B'

couple = {}

couple['A'] = get_random_entry()
couple['B'] = get_random_entry()

print(has_more_followers(couple))

print_entry(couple['A'], "Compare A")
print(art.vs)
print_entry(couple['B'], "Against B")

choice = input("Who has more followers? Type 'A' or 'B': ")

if choice == has_more_followers(couple):
    score += 1
    choice['A'] == couple[choice]
    couple['B'] = get_random_entry()
    print(f"You're right! Current score: {score}.")
else:
    print(f"Sorry that's wrong! Final score: {score}.")

