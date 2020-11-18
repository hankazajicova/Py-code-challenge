import random

user_possibilities = ["low", "high", "correct"]

def input_validator(user_input: str) -> bool:
    """user input validation

    Args:
        user_input (str): input string

    Returns:
        bool: validation
    """
    if user_input in user_possibilities:
        return True

    return False


# random approach
def guess_two_random() -> None:
    """
    guess and user (secret) number validation
    """
    min_value = 1
    max_value = 100
    number_of_guesses = 0
    while True:
        if (max_value - min_value) < 0:
            print("This is not in expected range 1 - 100. Game over.")
            return

        prog_guess = random.randint(min_value, max_value)
        print("My guess is : {prog_guess}".format(prog_guess = prog_guess))
        number_of_guesses += 1
        user_validation = input("correct, low or high? ")
        if not input_validator(user_validation):
            print("please, input if it's correct, low or high")
            continue

        if user_validation == "low":
            min_value = prog_guess + 1
        elif user_validation == "high":
            max_value = prog_guess - 1

        if user_validation == "correct":
            break

    print("Cool, your guess {guess} is correct. You guessed {number} times.".format(
        guess=prog_guess, number=number_of_guesses))

guess_two_random()


# faster approach
def guess_two_half() -> None:
    """
    guess and user (secret) number validation
    """
    min_value = 1
    max_value = 100
    number_of_guesses = 0
    while True:
        if (max_value - min_value) < 0:
            print("This is not in expected range 1 - 100. Game over.")
            return

        prog_guess = round((min_value + max_value)/2)
        print("My guess is : {prog_guess}".format(prog_guess = prog_guess))
        number_of_guesses += 1
        user_validation = input("correct, low or high? ")
        if not input_validator(user_validation):
            print("please, input if it's correct, low or high")
            continue

        if user_validation == "low":
            min_value = prog_guess
        elif user_validation == "high":
            max_value = prog_guess

        if user_validation == "correct":
            break

    print("Cool, your guess {guess} is correct. You guessed {number} times.".format(
        guess=prog_guess, number=number_of_guesses))

guess_two_half()
