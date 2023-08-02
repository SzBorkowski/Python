import random
guess = 0
while guess != "exit":
    x = random.randint(1, 9)
    print(x)
    tries = 0
    while guess != x and guess != "exit":
        guess = input("Guess a number between 1 and 9: ")
        tries += 1
        if guess == "exit":
            break
        elif int(guess) == x:
            if tries == 1:
                print("Correct! You guessed the number in ",tries,"try!")
                break
            else:
                print("Correct! You guessed the number in ",tries,"tries!")
                break
        elif int(guess) > x:
            print("Too high")
        elif int(guess) < x:
            print("Too low")