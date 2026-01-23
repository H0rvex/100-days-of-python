import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
player_choice = input("Rock, paper, or scissors?\n").lower()

if player_choice not in ["rock", "paper", "scissors"]:
    print("That’s not a valid choice.")
else:
    bot_choice = random.choice(choices)
    print(f"You chose:\n{eval(player_choice)}")
    print(f"Bot chose:\n{bot_choice}")

    if player_choice == "rock" and bot_choice == scissors:
        print("You win!")
    elif player_choice == "paper" and bot_choice == rock:
        print("You win!")
    elif player_choice == "scissors" and bot_choice == paper:
        print("You win!")
    elif bot_choice == eval(player_choice):
        print("It’s a tie!")
    else:
        print("You lose!")

print('Press "Ctrl + F5" to restart!')

