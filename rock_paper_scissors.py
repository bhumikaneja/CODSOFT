import random

print("===== ROCK PAPER SCISSORS =====")

options = ["rock", "paper", "scissors"]

play_game = "yes"

while play_game == "yes":

    player = input("\nChoose Rock, Paper or Scissors: ").lower()

    if player not in options:
        print("Please enter a valid choice.")
        continue

    computer = random.choice(options)

    print("Computer selected:", computer)

    if player == computer:
        print("Match Draw!")

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You won this round!")

    else:
        print("Computer won this round!")

    play_game = input("\nPlay again? (yes/no): ").lower()

print("Thanks for playing!")