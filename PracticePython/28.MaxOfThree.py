first = input("Insert the first variable: ")
second = input("Insert the second variable: ")
third = input("Insert the third variable: ")
if int(first) < int(second):
    if int(second) < int(third):
        print("Third variable is the largest.")
    else:
        print("Second variable is the largest.")
elif int(first) < int(third):
    if int(third) < int(second):
        print("Second variable is the largest.")
    else:
        print("Third variable is the largest.")
else:
    print("First variable is the largest.")