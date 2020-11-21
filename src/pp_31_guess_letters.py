# print("Welcome to Hangman!")
# word_to_guess = 'EVAPORATE'
# wrong_letters = []
# user_guess = ['_']*len(word_to_guess)
# print(' '.join(user_guess))


# def user_validation(input_str: str) -> bool:
#     """user input validation

#     Args:
#         input_str (str): user input

#     Returns:
#         bool: validity
#     """
#     if len(input_str) > 1:
#         print("You can guess only one letter in one turn. Try again!")
#         return False

#     return True


# def letter_evaluation(input_letter: str, input_word: str) -> bool:
#     """letter check

#     Args:
#         input_letter (str): user input
#         input_word (str): word to guess

#     Returns:
#         bool: letter presence
#     """
#     is_guessed = False
#     for i, inputs in enumerate(input_word):
#         if inputs == input_letter:
#             user_guess[i] = input_letter
#             is_guessed = True
#             continue

#     if is_guessed is True:
#         print(f"Correct. '{input_letter}' is there.")
#         print(' '.join(user_guess))
#         return True

#     wrong_letters.append(input_letter)
#     print(f"'{input_letter}' not there")
#     return False


# def main():
#     """hangman starter method
#     """
#     count_of_wrong_guesses = 6
#     while True:
#         user_input = input("Guess the letter: ").upper()

#         if not user_validation(user_input):
#             continue

#         if user_input in wrong_letters:
#             print(f"You have guessed this letter '{user_input}' already.")
#             continue


#         letter_check = letter_evaluation(user_input, word_to_guess)

#         if letter_check is False:
#             count_of_wrong_guesses -= 1

#         if count_of_wrong_guesses < 0:
#             print("You missed 6 times. Sorry you lost")
#             break
#         print(f"You can still guess {count_of_wrong_guesses} times wrongly.")

#         if '_' not in user_guess:
#             guessed = ''.join(user_guess)
#             print(f"Excellent! You guessed the word '{guessed}'.")
#             break

#     print("Game over")

# main()
