import random
list = []
with open("30.sowpods.txt", "r") as f:
    line = f.readline()
    while line:
        list.append(line)
        line = f.readline()
print(random.choice(list))