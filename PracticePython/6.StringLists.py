czyPalindrom = str(input("Wprowadź słowo, aby sprawdzić czy jest palindromem: "))
odbicie = czyPalindrom[::-1]
if czyPalindrom == odbicie:
    print("To słowo jest palindromem.")
else:
    print("To słowo nie jest palindromem.")

#2 sposób
def lustro(słowo):
    x = ""
    for i in range(len(słowo)):
        x += słowo[len(słowo)-1-i]
    return x

słowo = input("Wprowadź słowo, aby sprawdzić czy jest palindromem: ")
x = lustro(słowo)
if x == słowo:
    print("To słowo jest palindromem.")
else:
    print("To słowo nie jest palindromem.")