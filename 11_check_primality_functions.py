number = int(input("Give me number: "))


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
        if number % i == 0:
            list_of_divisors.append(i)
    list_of_divisors.append(number)
    return list_of_divisors


def is_prime(divisors: list) -> None:
    """find if the input number is prime or not

    Args:
        divisors (list): list of dividors from get_dividors
    """
    if len(divisors) == 2:
        print("Yes, this is prime number.")
    else:
        print("Nope, this is not prime number. Divisors are {divisors}".format(divisors=divisors))

divisors_of_number = get_divisors(number)
is_prime(divisors_of_number)
