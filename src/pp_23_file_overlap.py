from typing import List

with open('resources/primenumbers.txt', 'r') as prime_file:
    prime = prime_file.read().split('\n')
print(prime)


with open('resources/happynumbers.txt', 'r') as happy_file:
    happy = happy_file.read().split('\n')
print(happy)

common: List[str] = []
for i in prime:
    if i in happy:
        common.append(i)

print("The common numbers are: {common}".format(common=common))

prime_file.close()
happy_file.close()
