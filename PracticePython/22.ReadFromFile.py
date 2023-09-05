counter_dict = {}
with open('22.nameslist.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line = f.readline()

print(counter_dict)

#EXTRA
counter_dicty = {}
with open('22.Training_01.txt') as fy:
    liney = fy.readline()
    while liney:
        liney = liney[3:-26]
        if liney in counter_dicty:
            counter_dicty[liney] += 1
        else:
            counter_dicty[liney] = 1
        liney = fy.readline()

print(counter_dicty)