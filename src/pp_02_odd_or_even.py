number = int(input("Give me number: "))

if number % 4 == 0:
    print("you have chosen {number} which is even and also dividible by 4".format(number=number))
elif number % 2 == 0:
    print("you have chosen {number} which is even".format(number=number))
else:
    print("you have chosen {number} which is odd".format(number=number))

num = int(input("Give me another number: "))
check = int(input("and another one: "))

if num % check == 0:
    print("Your first number {num} is dividible by your second number {check}".format(
        num=num, check=check))
else:
    print("Your first number {num} is not dividible by your second number {check}".format(
        num=num, check=check))
    