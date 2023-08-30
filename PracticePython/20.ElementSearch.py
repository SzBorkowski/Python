import random

def binarysearch(list, element):
    start = 1
    end = len(list) - 1
    while True:
        middle = (end - start) / 2
        if middle < start or middle > end or middle < 0:
            return False
        middle = list[int(middle)]
        if middle == element:
            return True
        elif middle < element:
            end = middle
        else:
            start = middle

if __name__ == "__main__":
    randomlist = []
    for i in range(10):
        n = random.randint(0, 999)
        randomlist.append(n)
    randomlist.sort()
    print(randomlist)
    randomnumber = random.randint(0, 999)
    print(randomnumber)

    print(binarysearch(randomlist, randomnumber))

    l = [2, 4, 6, 8, 10]
    print(binarysearch(l, 5))
    print(binarysearch(l, 10))
    print(binarysearch(l, -1))
    print(binarysearch(l, 2))