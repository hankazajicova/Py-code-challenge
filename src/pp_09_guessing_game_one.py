import random


def guess_validator(input_guess: int) -> bool:
    """
    user guess validator

    Args:
        input_guess (int): user input integer

    Returns:
        bool: approval of the validation
    """
    if 1 <= input_guess <= 9:
        return True

    return False



def guess_the_number(rand_number: int, guess_input: str) -> bool:
    """
    Args:
        rand_number (int): input random number
        guess (str): user guessed number

    Returns:
        bool: approval of the validation
    """
    if guess_input == "exit":
        return True

    guess = int(guess_input)
    guess_validation = guess_validator(guess)

    if not guess_validation:
        print("You have to guess the number between 1 and 9 (included). Try again!")
        return False

    return evaluate_guess(rand_number, guess)


def evaluate_guess(rand_number: int, guess: int) -> bool:
    """
    guess and random number evaluation

    Args:
        rand_number (int): input random number
        guess (str): user guessed number

    Returns:
        bool: approval of the validation
    """
    if rand_number == guess:
        print("The number is {number}. You won!".format(number=rand_number))
        return True

    if guess < rand_number:
        print("Your guess {guess} is lower than the number. Guess again".format(guess=guess))
    elif guess > rand_number:
        print("Your guess {guess} is higher than the number. Guess again".format(guess=guess))

    return False



def guess_game():
    """
    starter of the guess game
    """
    random_number = random.randint(1, 9)
    #print(random_number)
    number_of_guesses = 0
    while True:
        user_guess = input("Guess the number between 1 and 9 (included): ")
        game_state = guess_the_number(random_number, user_guess)
        number_of_guesses += 1
        if game_state is False:
            continue

        if game_state is True:
            break

    print("You guessed {number} times. Enjoyed? Good. Try again.".format(number=number_of_guesses))

guess_game()
