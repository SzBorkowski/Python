import os
from blind_art import logo

print(logo)

bidding = True
bidders = {}
while bidding:
  name = input("What's your name? ")
  bid = int(input("What's your bid? $"))
  bidders[name] = bid
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if should_continue == "no":
    bidding = False
  else:
    os.system('cls')
highest_bid = 0
for bidder in bidders:
  if bidders[bidder] > highest_bid:
    highest_bid = bidders[bidder]
    winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}")