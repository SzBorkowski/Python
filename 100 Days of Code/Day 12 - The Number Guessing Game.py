import random

num = random.randint(1, 100)
print("Welcome to the number guessing game.")
print("I'm thinking of a number between 1 and 100.")
#Uncomment below line to see which number is it
#print(num)
difficulty = input('Choose a difficulty level. Type "easy" or "hard": ')
if difficulty == "easy":
  turns = 10
else:
  turns = 5

#game commences
while turns > 0:
  print(f"You have {turns} guesses.")
  guess = int(input("Make a guess: "))
  if guess > num:
      print("Too high.")
  elif guess < num:
    print("Too low.")
  else:
    print("You got it!")
    print("The number was", num)
    break
  turns -= 1
  if turns == 0:
    print("You ran out of turns.")
    print("The number was ", num)