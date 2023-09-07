size = int(input("What size game board do you want to play? "))
for i in range (size):
    print(" ---" * size)
    print("|   " * (size + 1))
print(" ---" * size)

"""Using functions
def floors():
    print(" ---" * size)

def walls():
    print("|   " * (size + 1))

for i in range(size):
    floors()
    walls()
floors()"""