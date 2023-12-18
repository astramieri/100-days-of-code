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

def calculate_score(cards):
    """Returns the score calculated from the cards."""
    score = 0

    for card in cards:
        if card == 'A':
            score += 11
        elif card in ['J', 'Q', 'K']:
            score += 10
        else:
            score += int(card)

        if score > 21:
            if card == 'A':
                score -= 10

    if score == 21:
        if len(cards) == 2:
            score = 0 # blackjack

    return score

def play_game():
    print(logo)

    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(new_card())
        computer_cards.append(new_card())

    

want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
while want_to_play == 'y':
    play_game()

# if play == 'y':
#     is_game_over = False

#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)

#         print(f"Your cards: {user_cards}, current score: {user_score}")
#         print(f"Computer first card: {computer_cards[0]}")

#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             more_cards = input("Do you want another card? Type 'y' or 'n' to pass: ")

#             if more_cards == 'y':
#                 user_cards.append(new_card())