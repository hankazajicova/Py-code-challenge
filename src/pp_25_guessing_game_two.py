import random


def input_validator(input_number: int) -> bool:
    """
    user guess validator

    Args:
        input_guess (int): user input integer

    Returns:
        bool: approval of the validation
    """
    if 1 <= input_number <= 9:
        return True

    return False


def guess_the_number(input_number: int, guess_number: int) -> dict:
    """
    Args:
        input_number (int): user input number
        guess_number (int): by programe guess number

    Returns:
        dict: validation
    """
    if not input_validator(input_number):
        print("You have to give me the number between 1 and 9 (included). Try again!")
        return False

    return evaluate_guess(input_number, guess_number)


def evaluate_guess(user_input: int, guess_number: int) -> dict:
    """
    guess and input number evaluation

    Args:
        user_input (int): user input number
        guess_number (int): by programme guessed number

    Returns:
        dict: dictionary with min and max value
    """
    min_num = 1
    max_num = 9

    if user_input == guess_number:
        print("The number is {number}. You won!".format(number=user_input))
        return {
            'min' : min_num,
            'max' : max_num
            }

    if guess_number < user_input:
        min_num = guess_number + 1
        print("Your guess {guess} is lower than the number. Guess again".format(guess=guess_number))
    elif guess_number > user_input:
        max_num = guess_number - 1
        print("Your guess {guess} is higher than the number. Guess again".format(
            guess=guess_number))

    return {
        'min' : min_num,
        'max' : max_num
        }


def guess_game_two():
    """
    starter of the guess game two
    """
    user_input = int(input("Give me the number between 1 and 9 (included): "))
    print(user_input)
    number_of_guesses = 0
    min_num = 1
    max_num = 9
    while True:
        guess_number = random.randint(min_num, max_num)
        print("Program guessed number: {guess_number}.".format(guess_number=guess_number))
        game_state = guess_the_number(user_input, guess_number)
        number_of_guesses += 1

        min_num = game_state['min']
        max_num = game_state['max']
        print("min is {min} and max is {max}".format(min=min_num, max=max_num))

        if game_state['min'] == 1 and game_state['max'] == 9:
            break

    print("Hey Program! You guessed {number} times. Enjoyed? Good. Try again.".format(
        number=number_of_guesses))

guess_game_two()
