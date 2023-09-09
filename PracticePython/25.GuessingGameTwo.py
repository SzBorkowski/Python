import random
"""
input("Pick a number between 0 and 100 and I will try to guess it.")
guess = random.randint(0, 100)
while True:
    decision = input("Is it "+str(guess)+"? (Correct, too high, too low) ")
    if decision == "correct":
        print("Yay!")
        break
    if decision == "too high":
        guess = random.randint(0, guess)
    if decision == "too low":
        guess = random.randint(guess, 100)"""

input("Pick a number between 0 and 100 and I will try to guess it.")
guess = random.randint(0, 100)
guesslist = list(range(0, 100))
while True:
    decision = input("Is it "+str(guess)+"? (Correct, too high, too low) ")
    if decision == "correct":
        print("Yay!")
        break
    if decision == "too high":
        while True:
            guesslist.remove(guess)
            guess += 1
            if guess == guesslist[len(guesslist)-1]:
                break
        guess = random.choice(guesslist)
    if decision == "too low":
        while True:
            guesslist.remove(guess)
            guess -= 1
            if guess == guesslist[0]:
                break
        guess = random.choice(guesslist)