from highlow_art import logo, vs
from highlow_data import data
import random
import os

#Get random accounts
def random_account():
  random_account = random.choice(data)
  return random_account

#Checking whether the accounts are the same
def check_account(first,second):
  while True:
    if first == second:
      second = random.choice(data)
    else:
      break

#Check which option is correct
def check_decision(dec):
  while True:
    global score, a, game
    if decision == "A":
      if a["follower_count"] > b["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}.")
        a = b
        break
      else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game = "end"
        break
    elif decision == "B":
      if a["follower_count"] < b["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}.")
        a = b
        break
      else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game = "end"
        break

#Main loop
def continuation():
  while True:
    global decision, b
    os.system('cls')
    print(logo)
    check_decision(decision)
    if game == "end":
      break
    print(f"Compare A: {a['name']} - {a['description']} from {a['country']}.")
    print(vs)
    b = random_account()
    print(f"Against B: {b['name']} - {b['description']} from {b['country']}.")
    decision = input("Who has more followers? Type A or B: ")

#Setting the basic variables
a = random_account()
b = random_account()
score = 0
game = None

#Main program
check_account(a,b)
print(logo)
print(f"Compare A: {a['name']} - {a['description']} from {a['country']}.")
print(vs)
print(f"Against B: {b['name']} - {b['description']} from {b['country']}.")
decision = input("Who has more followers? Type A or B: ")
continuation()