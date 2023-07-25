num = int(input("Enter a number you want to find divisors for: "))
x = range(1, num+1)
divisors = []
for element in x:
    if num % element == 0:
        divisors.append(element)
print(divisors)