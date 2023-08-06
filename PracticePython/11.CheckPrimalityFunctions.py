num = int(input("Enter a number you want to check if it is a prime number: "))
x = range(1, num+1)
divisors = []
for element in x:
    if num % element == 0:
        divisors.append(element)
if len(divisors) > 2:
    print(num," is not a prime number.")
else:
    print(num," is a prime number.")