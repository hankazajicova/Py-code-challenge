from datetime import datetime

name = input("your name: ")
age = int(input("your age: "))


today = datetime.now()
current_year = today.year

year = current_year + (100 - age)
message = "Hi {name}, so if you are {age} now, then you will be in {year} 100 years old".format(
    name=name.title(),
    age=str(age),
    year=year)
print(message)


set_number = int(input("so {name}, give me number: ".format(name=name.title())))
message += "\n"
print(message * set_number)
