number = int(input("Enter a number to check: "))
divider = int(input("Enter a number to divide by: "))
if number % 4 == 0:
    print("That number is a multiple of 4. That is an even number.")
elif number % 2 == 0:
    print("That is an even number.")
else:
    print("That is an odd number.")

if number % divider == 0:
    print(number, " divides evenly by ", divider, ".")
else:
    print(number, " doesn't divide evenly by ", divider, ".")