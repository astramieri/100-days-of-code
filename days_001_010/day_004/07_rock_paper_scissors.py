# Roc, Paper, Scissors
import random

shapes = ["Rock", "Paper", "Scissors"]

player = int(input(f"What do you choose (0={shapes[0]}, 1={shapes[1]}, 2={shapes[2]})? "))

print(f"Player has chosen: {shapes[player]}")

computer = random.randint(0, 2)

print(f"Computer has chosen: {shapes[int(computer)]}")

if player == computer:
    print("You draw. 😑")
elif (player == computer + 1) or (player == 0 and computer == 2):
    print("You win! 😆")
else:
    print("You lose. 😓")
