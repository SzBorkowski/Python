print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
perc = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip = perc / 100 * bill
bill_per_person = (bill + tip) / people
final_bill = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_bill}")