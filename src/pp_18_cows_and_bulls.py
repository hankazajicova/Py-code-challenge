import random

MIN_VALUE = 1000
MAX_VALUE = 9999

def input_validation(input_number: str) -> bool:
    """user input validation

    Args:
        input_number (str): user inputed number

    Returns:
        bool: valid or not
    """
    try:
        number = int(input_number)
    except ValueError:
        return False

    if MIN_VALUE <= number <= MAX_VALUE:
        return True

    return False


def get_random_number() -> list:
    """generates a random 4 digit number, transform each digit into the list

    Returns:
        list: list of random numbers
    """
    number = random.randint(MIN_VALUE, MAX_VALUE)
    digits = [int(x) for x in str(number)]
    #print(number)
    #print(digits)
    return digits


def number_to_indices(input_number: str) -> list:
    """user input number transformed into the list

    Args:
        input_number (str): user input

    Returns:
        list: list of user input numbers
    """
    digits_input = [int(x) for x in str(input_number)]
    #print(digits_input)
    return digits_input


def compare_indices(random_num: list, input_num: list):
    """compares each indeces of input and random numbers

    Args:
        random_num (list): randomly generated in get_random_number
        input_num (list): inputed by user and validated above

    Returns:
        list, int: list of correctly guessed numbers with position and almost guessed,
        cows and bulls score
    """
    guessed_correctly = [None] * 4
    almost_guessed = []

    for i, inputs in enumerate(input_num):
        if inputs == random_num[i]:
            guessed_correctly[i] = random_num[i]
        elif inputs in random_num:
            almost_guessed.append(inputs)
            print("number {i} is there but somewhere else.".format(i=inputs))

    #print(almost_guessed)
    print(guessed_correctly)
    return {
        'guessed_correctly' : guessed_correctly,
        'almost_guessed' : almost_guessed
        }


def count_non_none(input_lst: list) -> int:
    """calculation of the count of the not None elements in list

    Args:
        input_lst (list): input list

    Returns:
        int: count of the not None elements in list
    """
    return len(input_lst) - input_lst.count(None)


def main():
    """
    starter for comparison
    conditional validation
    """
    rnd_number = get_random_number()
    # bulls = 0
    almost_guessed = []
    while True:
        guess_four_digits = input("Guess four digits number: ")
        if not input_validation(guess_four_digits):
            print("Input number must have four digits. Try again!")
            continue
        inp_number = number_to_indices(guess_four_digits)

        compare = compare_indices(rnd_number, inp_number)

        cows = count_non_none(compare['guessed_correctly'])
        almost_guessed = almost_guessed + compare['almost_guessed']
        almost_guessed = list(set(almost_guessed))
        bulls = len(almost_guessed)

        print("Almost guessed are {almost_guessed}".format(almost_guessed=almost_guessed))
        print("{cows} cows, {bulls} bulls".format(cows=cows, bulls=bulls))
        if None not in compare['guessed_correctly']:
            break

    print("That's it!")

main()
