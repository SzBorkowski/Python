a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [x for x in a if x in b]
c = [*set(c)]
print(c)

import random
randlist1 = random.sample(range(1,10), 6)
randlist2 = random.sample(range(1,10),8)
result_overlaps = [i for i in set(randlist1) if i in randlist2]
result = [i for i in result_overlaps if result_overlaps.count(i) == 1]
print(randlist1)
print(randlist2)
print(result)