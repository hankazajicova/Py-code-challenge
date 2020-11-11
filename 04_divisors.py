number = int(input("Give me number: "))

divisors = []

x = range(1, int(number/2) + 1)
for i in x:
    if number % i == 0:
        divisors.append(i)
divisors.append(number)
print(divisors)
