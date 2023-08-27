import random

randomlist = []
for i in range(10):
    n = random.randint(0, 999)
    randomlist.append(n)
randomlist.sort()
print(randomlist)
randomnumber = random.randint(0, 999)
print(randomnumber)

if randomnumber in randomlist:
    print(str(randomnumber)+" is present inside the random list.")
else:
    print(str(randomnumber) + " is not present inside the random list.")

if len(randomlist) % 2 == 0:
    middle = len(randomlist) / 2
    shortlist = randomlist[0, middle]
    print(shortlist)
else:
    middle = len(randomlist) / 2 + 1
    shortlist = randomlist[0, middle]
    print(shortlist)