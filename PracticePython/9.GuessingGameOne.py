#work in progress
import random
while True:
    x = random.randint(1, 9)
    print(x)
    guess = "play"
    while True and guess != "exit":
        guess = input("Guess a number between 1 and 9: ")
        if int(guess) == x:
            print("Correct!")
            break
        elif int(guess) > x:
            print("Too high")
        elif int(guess) < x:
            print("Too low")