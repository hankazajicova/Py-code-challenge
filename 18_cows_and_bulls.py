import random


def input_validation(input_number: str) -> bool:
    """user input validation

    Args:
        input_number (str): user inputed number

    Returns:
        bool: valid or not
    """
    input_number = int(input_number)
    if 1000 <= input_number <= 9999:
        return True

    return False


def get_random_number() -> list:
    """generates a random 4 digit number, transform each digit into the list

    Returns:
        list: list of random numbers
    """
    number = random.randint(1000,9999)
    digits = [int(x) for x in str(number)]
    print(number)
    return [digits]


def number_to_indices(input_number: str):
    """user input number transformed into the list

    Args:
        input_number (str): user input

    Returns:
        bool, list: False if validation is not true, elif returns list
    """
    validate = input_validation(input_number)
    if not validate:
        print("Input number must have four digits. Try again!")
        return False
    elif validate is True:
        digits_input = [int(x) for x in str(input_number)]
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
    cows = 0
    bulls = 0
    guessed_correctly = [None] * 4
    almost_guessed = []

    for i in range(len(input_num)):
        if input_num[i] == random_num[i]:
            cows += 1
            guessed_correctly[i] = random_num[i]

    for i in input_num:
        if i in random_num and i not in guessed_correctly:
            bulls += 1
            almost_guessed.append(i)
            print("number {i} is there but somewhere else.".format(i=i))

    print(guessed_correctly)
    return guessed_correctly, bulls, cows, almost_guessed


def main():
    """
    starter for comparison
    conditional validation
    """
    rnd_number = get_random_number()
    bulls_in = 0
    guessed_almost = []
    while True:
        guess_four_digits = input("Guess four digits number: ")
        inp_number = number_to_indices(guess_four_digits)
        if inp_number is False:
            while True:
                guess_four_digits = input("Guess again: ")
                inp_number = number_to_indices(guess_four_digits)
                if inp_number is False:
                    continue

                break

        cows_in = 0
        compare = compare_indices(rnd_number, inp_number)
        bulls_in += compare[1]
        print("bulls are: {bulls_in}".format(bulls_in=bulls_in))
        cows_in += compare[2]
        guessed_almost = guessed_almost + compare[3]
        for i in guessed_almost:
            if guessed_almost.count(i) >= 2:
                bulls_in -= 1
                guessed_almost = list(set(guessed_almost))
                break
        print("Almost guessed are {guessed_almost}".format(guessed_almost=guessed_almost))
        print("{cows} cows, {bulls} bulls".format(cows=cows_in, bulls=bulls_in))
        if None not in compare[0]:
            break

    print("That's it!")

main()
