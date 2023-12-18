import random
from blackjack_art import logo
import os


# function for drawing cards by player
def player_move():
    while True:

        # player has over 21 points and an ace
        if sum(player) > 21 and 11 in player:
            for i in range(len(player)):
                if player[i] == 11:
                    player[i] = 1

        # show the cards
        print(f"Your cards: {player}, current score: {sum(player)}")
        print(f"Dealer's first card: {dealer[0]}")

        # player has over 21 points
        if sum(player) > 21:
            break

        # draw another card decision
        if input("Do you want another card? (y/n) ") == "y":
            player.append(random.choice(cards))
        else:
            break


# function for adding cards to a dealer
def dealer_move():
    while True:

        # dealer has over 21 points and an ace
        if sum(dealer) > 21 and 11 in dealer:
            for i in range(len(dealer)):
                if dealer[i] == 11:
                    dealer[i] = 1

        # dealer has below 17 points (has to draw)
        if sum(dealer) < 17:
            dealer.append(random.choice(cards))
        else:
            break


def winner():
    print(f"Your cards: {player}, score: {sum(player)}")
    print(f"Dealer's cards: {dealer}, score: {sum(dealer)}")
    if sum(dealer) > 21:
        print("You win.")
    elif sum(player) > sum(dealer):
        print("You win.")
    elif sum(player) < sum(dealer):
        print("You lose.")
    else:
        print("Draw.")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    if input("Do you want to play Blackjack? (y/n) ") == "y":
        player = [random.choice(cards), random.choice(cards)]
        dealer = [random.choice(cards), random.choice(cards)]
        os.system('cls')
        print(logo)
        player_move()
        if sum(player) > 21:
            print("You lose.")
        else:
            dealer_move()
            winner()
    else:
        break