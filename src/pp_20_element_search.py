import random


def get_random_list() -> list:
    """random list generator
    Returns:
        list: random list
    """
    list_1 = []
    for _ in range(0, 10):
        n = random.randint(1, 20)
        list_1.append(n)
    list_1.sort()
    print(list_1)
    return list_1


def is_inside(input_list: list, input_value: int) -> bool:
    """check if user input number is inside random list

    Args:
        input_list (list): random list created above
        input_value (int): user input value

    Returns:
        bool: True if the number is inside
    """
    if input_value in input_list:
        print("Yep, number {input_value} is inside the random list.".format(
            input_value=input_value))
        return True

    return False


if __name__ == "__main__":
    user_number = int(input("Give me a number 1 - 20: "))
    rnd_list = get_random_list()
    in_or_not = is_inside(rnd_list, user_number)
    print(in_or_not)
