name = input("Enter your name: ")
age = int(input("Enter your age: "))
import datetime
x = datetime.datetime.now()
currentyear = x.year
yearof100 = currentyear - age + 100
print ("Hello, "+name+"! You will turn 100 years old in "+str(yearof100)+".")

"""
EXTRA
reps = int(input("How many messages do you wish to see?:"))
print(reps * "All right""\n")
"""