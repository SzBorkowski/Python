import random

def random4s():
    randlist = []
    for i in range(0,4):
        n = random.randint(0,9)
        randlist.append(n)
    return randlist

guessthat = random4s()
print(guessthat)
user4s = input("Guess a 4-digit number: ")
guesslist = [int(x) for x in str(user4s)]
print(guesslist)
if len(guesslist) != 4:
    print("That is not a 4-digit number. Try again.")
else:
    