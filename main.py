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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("Invalid number! You lose")
else:
  if user_choice == 0:
    print(rock)
  elif user_choice == 1:
    print(paper)
  elif user_choice == 2:
    print(scissors)

  print("Computer chose:")
  random_integer = random.randint(0, 2)
  if random_integer == 0:
    print(rock)
  elif random_integer == 1:
    print(paper)
  elif random_integer == 2:
    print(scissors)

  # Rock wins against scissors.
  # Scissors win against paper.
  # Paper wins against rock.

  if user_choice == random_integer:
    print("Tie")
  elif user_choice == 0 and random_integer == 2:
    print("You win")
  elif user_choice == 2 and random_integer == 1:
    print("You win")
  elif user_choice == 1 and random_integer == 0:
    print("You win")
  else:
    print("You lose")

