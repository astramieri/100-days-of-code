import os
import random
from art import logo

def new_random_card():
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return cards[random.randint(1, len(cards))]

while True:
    print(logo)

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play == 'n':
        break

    your_cards = []
    your_cards.append(new_random_card())
    your_cards.append(new_random_card())

    print(f"Your cards: {your_cards}")

    break # TOFIX