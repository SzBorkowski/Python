import random

input("Pick a number between 0 and 100 and I will try to guess it.")
guess = random.randint(0, 100)
guesslist = list(range(0, 101))
tries = 0
while True:
    decision = input("Is it "+str(guess)+"? (Correct, too high, too low) ")
    if decision == "correct":
        tries += 1
        if tries == 1:
            print("Wow! It took me " + str(tries) + " try to guess it!")
        print("Yay! It took me "+str(tries)+" tries to guess it!")
        break
    if decision == "too high":
        tries += 1
        if guess == 0:
            print("But that's the lowest number possible!")
            break
        i = guess
        length = len(guesslist)
        while True:
            if guess == guesslist[-1]:
                guesslist.remove(guess)
                break
            guesslist.remove(guess)
            guess += 1
        guess = random.randint(guesslist[0], i-1)
    if decision == "too low":
        tries += 1
        if guess == 100:
            print("But that's the highest number possible!")
            break
        i = guess
        while True:
            if guess == guesslist[0]:
                guesslist.remove(guess)
                break
            guesslist.remove(guess)
            guess -= 1
        guess = random.randint(i+1, guesslist[-1])