import random

def get_first_last() -> list:
    """creates random list and assign a new list its first and last element

    Returns:
        list: output list of first and last element from random list
    """
    random_list = []
    for _ in range(0, 10):
        n = random.randint(1, 20)
        random_list.append(n)
    random_list.sort()
    print(random_list)

    first_last = []
    first_last.append(random_list[0])
    first_last.append(random_list[-1])
    return first_last

list_first_last = get_first_last()
print(list_first_last)
