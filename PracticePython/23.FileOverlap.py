primes = []
with open('23.primenumbers.txt') as f:
    line = f.readline()
    while line:
        primes.append(int(line))
        line = f.readline()

happies = []
with open('23.happynumbers.txt') as f:
    line = f.readline()
    while line:
        happies.append(int(line))
        line = f.readline()

happyprimes = []
for elem in primes:
    if elem in happies:
        happyprimes.append(elem)
# happyprimes = [elem for elem in primes if elem in happies]
print(happyprimes)


# 2 way
def filetolistofints(filename):
    list_to_return = []
    with open(filename) as f:
        line = f.readline()
        while line:
            list_to_return.append(int(line))
            line = f.readline()
    return list_to_return


primeslist = filetolistofints('23.primenumbers.txt')
happieslist = filetolistofints('23.happynumbers.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)
