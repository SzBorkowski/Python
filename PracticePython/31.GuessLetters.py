word = "EVAPORATE"
guess = "_" * len(word)
word = list(word)
guess = list(guess)
letter = input("Pick a letter: ")
alreadyGuessed = []
while True:
    if letter.upper() in alreadyGuessed:
        letter = ""
        print("This letter was already guessed.")
    elif letter.upper() in word:
        index = word.index(letter.upper())
        guess[index] = letter.upper()
        word[index] = "_"
    else:
        print("".join(guess))
        if letter is not "":
            alreadyGuessed.append(letter.upper())
        letter = input("Pick a letter: ")
    if "_" not in guess:
        print("You won!")
        break