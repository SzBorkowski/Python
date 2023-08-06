def Fibonacci():
    num = int(input("How many Fibonacci numbers to generate? "))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1, 1]
    elif num > 2:
        fib = [1, 1]
        while i < num:
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

print(Fibonacci())