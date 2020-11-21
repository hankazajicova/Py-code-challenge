import random

with open('resources/sowpods.txt', 'r') as sowpods:
    all_text = sowpods.read().split('\n')
    # print(all_text)

    random_word = random.choice(all_text)
    # print(random_word)

sowpods.close()


word_to_guess = random_word
wrong_letters = []
user_guess = ['_']*len(word_to_guess)
print(' '.join(user_guess))


def user_validation(input_str: str) -> bool:
    '''user input validation

    Args:
        input_str (str): user input

    Returns:
        bool: validity
    '''
    if len(input_str) > 1:
        print('You can guess only one letter in one turn. Try again!')
        return False

    return True


def letter_evaluation(input_letter: str, input_word: str) -> bool:
    '''letter check

    Args:
        input_letter (str): user input
        input_word (str): word to guess

    Returns:
        bool: letter presence
    '''
    is_guessed = False
    for i, inputs in enumerate(input_word):
        if inputs == input_letter:
            user_guess[i] = input_letter
            is_guessed = True
            continue

    if is_guessed is True:
        print(f'Correct. "{input_letter}" is there.')
        print(' '.join(user_guess))
        return True

    wrong_letters.append(input_letter)
    print(f'"{input_letter}" not there')
    return False


def get_hangman(count_of_wrong_guesses: int) -> None:
    """get hangman picture

    Args:
        count_of_wrong_guesses (int): count of wrong guesses
    """
    if count_of_wrong_guesses == 5:
        print('')
        print('  o')
    elif count_of_wrong_guesses == 4:
        print('')
        print('  o')
        print(' /')
    elif count_of_wrong_guesses == 3:
        print('')
        print('  o')
        print(' /|')
    elif count_of_wrong_guesses == 2:
        print('')
        print('  o')
        print(' /|\\ ')
    elif count_of_wrong_guesses == 1:
        print('')
        print('  o')
        print(' /|\\ ')
        print(' /')
    elif count_of_wrong_guesses == 0:
        print('')
        print('  o')
        print(' /|\\ ')
        print(' / \\ ')
    elif count_of_wrong_guesses < 0:
        print('______')
        print('|    | ')
        print('|    o')
        print('|   /|\\ ')
        print('|   / \\ ')
        print('|_________')


def main():
    '''hangman starter method
    '''
    print('Welcome to Hangman!')
    count_of_wrong_guesses = 6
    while True:
        user_input = input('Guess the letter: ').upper()

        if not user_validation(user_input):
            continue

        if user_input in user_guess:
            print(f'You have guessed "{user_input}" already. Try again.')
            continue

        if user_input in wrong_letters:
            print(f'You have tried "{user_input}" already. Try again.')
            continue

        letter_check = letter_evaluation(user_input, word_to_guess)

        if letter_check is False:
            count_of_wrong_guesses -= 1

        get_hangman(count_of_wrong_guesses)

        if count_of_wrong_guesses < 0:
            print('You missed 6 times. Sorry you lost')
            break

        if '_' not in user_guess:
            guessed = ''.join(user_guess)
            print(f'Excellent! You guessed the word "{guessed}".')
            break

    print('Game over')

main()
