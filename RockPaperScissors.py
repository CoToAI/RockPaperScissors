import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

gameImages = [Rock, Paper, Scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if player >= 0 and player <= 2:
    print(gameImages[player])

computer = random.randint(0, 2)
print("Computer chose: ")
print(gameImages[computer])


if player >= 3 or player < 0:
    print(f"Not a valid number! You lose! {player}")
elif player == 0 and computer == 2:
    print("You win!")
elif computer == 0 and player == 2:
    print("You lose!")
elif computer > player:
    print("You lose!")
elif player > computer:
    print("You win!")
elif player == computer:
    print("It's a draw!")




