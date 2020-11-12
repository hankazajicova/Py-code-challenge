import random


rnd_list_1 = []
rnd_list_2 = []

for i in range(0, 10):
    n = random.randint(1, 40)
    rnd_list_1.append(n)
rnd_list_1.sort()
print(rnd_list_1)

for i in range(0, 12):
    n = random.randint(1, 40)
    rnd_list_2.append(n)
rnd_list_2.sort()
print(rnd_list_2)


common_elements = [i for i in rnd_list_1 if i in rnd_list_2]
common_elements = list(dict.fromkeys(common_elements))
print(common_elements)
