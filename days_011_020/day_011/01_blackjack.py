import os
import random
from art import logo

# The deck is unlimited in size.
# The Jack/Queen/King all count as 10.
# The Ace can count as 1 or 11.
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def new_card():
    """Returns a random card from the deck."""
    #return cards[random.randint(1, len(cards))]
    card = random.choice(cards)
    return card

your_cards = []
computer_cards = []

for i in range(2):
    your_cards.append(new_card())
    computer_cards.append(new_card())

def get_score(cards):
    score = 0

    for card in cards:
        if card == 'A':
            score += 10
        elif card in ['J', 'Q', 'K']:
            score += 10
        else:
            score += int(card)

        if score > 21:
            pass # TOFIX


    return score

while True:
    print(logo)

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play == 'n':
        break


    your_cards.append(new_random_card())
    your_cards.append(new_random_card())

    print(f"Your cards: {your_cards}")


    computer_cards.append(new_random_card())
    computer_cards.append(new_random_card())

    print(f"Computer first card: {computer_cards[0]}")

    while True:
        more_cards = input("Do you want another card? Type 'y' or 'n' to pass: ")

        if more_cards == 'n':
            break

        your_cards.append(new_random_card())

        print(f"Your cards: {your_cards}")

        your_score = get_score(your_cards)

        if your_score > 21:
            print("You lose")
            break # TOFIX
            

    break