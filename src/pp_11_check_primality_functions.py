from typing import List


def get_divisors(input_number: int) -> list:
    """find divisors of input number

    Args:
        input_number (int): user defined input number

    Returns:
        list: list of dividors of input number
    """
    list_of_divisors = []
    x = range(1, int(input_number/2) + 1)
    for i in x:
        if input_number % i == 0:
            list_of_divisors.append(i)
    list_of_divisors.append(input_number)
    return list_of_divisors


def is_prime(divisors: List[int]) -> bool:
    """find if the input number is prime or not

    Args:
        divisors (list): list of dividors from get_dividors
    """
    if len(divisors) == 2:
        print("Yes, this is prime number.")
        return True

    print("Nope, this is not prime number. Divisors are {divisors}".format(divisors=divisors))
    return False


if __name__ == "__main__":
    number = int(input("Give me number: "))
    divisors_of_number = get_divisors(number)
    is_prime(divisors_of_number)
