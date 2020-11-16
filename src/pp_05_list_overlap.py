from typing import List
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c: List[int] = []
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)


randomList_1 = []
randomList_2 = []

for i in range(0, 10):
    n = random.randint(1, 20)
    randomList_1.append(n)
randomList_1.sort()
print(randomList_1)

for i in range(0, 12):
    n = random.randint(1, 20)
    randomList_2.append(n)
randomList_2.sort()
print(randomList_2)

common = [i for i in randomList_1 if i in randomList_2]
common = list(dict.fromkeys(common))
print('common:', common)
