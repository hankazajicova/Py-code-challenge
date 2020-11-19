import random

START_MIN_VALUE = 1
START_MAX_VALUE = 100

LOW_INPUT = "low"
HIGH_INPUT = "high"
CORRECT_INPUT = "correct"

USER_POSSIBILITIES = [LOW_INPUT, HIGH_INPUT, CORRECT_INPUT]

def input_validator(user_input: str) -> bool:
    """user input validation

    Args:
        user_input (str): input string

    Returns:
        bool: validation
    """
    if user_input in USER_POSSIBILITIES:
        return True

    return False


# random approach
def guess_two_random() -> None:
    """
    guess and user (secret) number validation
    """
    min_value = START_MIN_VALUE
    max_value = START_MAX_VALUE
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

        if user_validation == LOW_INPUT:
            min_value = prog_guess + 1
        elif user_validation == HIGH_INPUT:
            max_value = prog_guess - 1

        if user_validation == CORRECT_INPUT:
            break

    print("Cool, your guess {guess} is correct. You guessed {number} times.".format(
        guess=prog_guess, number=number_of_guesses))

guess_two_random()


# half approach
def guess_two_half() -> None:
    """
    guess and user (secret) number validation
    """
    min_value = START_MIN_VALUE
    max_value = START_MAX_VALUE
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

        if user_validation == LOW_INPUT:
            min_value = prog_guess
        elif user_validation == HIGH_INPUT:
            max_value = prog_guess

        if user_validation == CORRECT_INPUT:
            break

    print("Cool, your guess {guess} is correct. You guessed {number} times.".format(
        guess=prog_guess, number=number_of_guesses))

guess_two_half()
