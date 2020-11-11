a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# first task
b = []
for i in a:
    if i < 5:
        b.append(i)
print('b:', b)

# second task
c = [i for i in a if i < 5]
print('c:', c)

# third task
number = int(input("Hi, give me number: "))

d = []
for i in a:
    if i < number:
        d.append(i)
print('d:', d)
