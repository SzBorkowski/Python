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

import random
computer_pick = random.randint(0, 2)
if computer_pick == 0:
  computer_pick = rock
elif computer_pick == 1:
  computer_pick = paper
else:
  computer_pick = scissors

pick = input("What do you pick? Rock, paper or scissors? ")
if pick == "rock":
  pick = rock
elif pick == "paper":
  pick = paper
else:
  pick = scissors

print(pick)
print("Computer chose:")
print(computer_pick)

if computer_pick == rock and pick == scissors:
  print("Computer wins!")
elif computer_pick == paper and pick == rock:
  print("Computer wins!")
elif computer_pick == scissors and pick == paper:
  print("Computer wins!")
elif computer_pick == pick:
  print("It's a tie!")
else:
  print("You win!")