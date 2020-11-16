input_string = input("Give me string🔫: ")

input_string = input_string.replace(' ', '')


def is_palindromic(string: str) -> str:
    """Is string palindromic

    Args:
        string (str): input string
    Returns:
        str: result if the string is palindromic
    """
    half_the_length = int(len(string)/2)
    for i in range(half_the_length):
        if string[i] != string[-i-1]:
            return "💥"

    return "Yep it is"

result = is_palindromic(input_string)
print(result)
