input_sentence = input("Type any sentence: ")


# first approach with reverse()
def get_reverse(input_str: str) -> str:
    """get reverse order of words with reverse() method

    Args:
        input_str (str): user input sentence

    Returns:
        str: reversed order of input sentence
    """
    splitted = input_str.split()
    splitted.reverse()
    new_order = ' '.join(splitted)
    return new_order

reverse_order = get_reverse(input_sentence)
print(reverse_order)


# second approach with list order
def get_reverse_order(input_str: str) -> str:
    """"get reverse order of words with element order

    Args:
        input_str (str): user input sentence

    Returns:
        str: reversed order of input sentence
    """
    splitted = input_str.split()
    new_order = splitted[::-1]
    new_order = ' '.join(new_order)
    return new_order

reverse = get_reverse_order(input_sentence)
print(reverse)
