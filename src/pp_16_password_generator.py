import random
import string

pw_strength = ["weak", "medium", "strong"]

lower = string.ascii_lowercase
upper = string.ascii_uppercase
nums = string.digits
characters = string.punctuation


def input_validation(user_input: str) -> bool:
    """user input validator

    Args:
        user_input (str): user input pw strength

    Returns:
        bool: evaluation of the validation
    """
    if user_input in pw_strength:
        return True

    return False


def get_weak_pw() -> list:
    """generator for strong pw characters

    Returns:
        list: list of output randomly generated characters
    """
    l = random.choices(lower, k=4)
    u = random.choices(upper, k=2)
    n = random.choices(nums, k=2)
    weak_password = l + u + n
    return weak_password


def get_medium_pw() -> list:
    """generator for strong pw characters

    Returns:
        list: list of output randomly generated characters
    """
    l = random.choices(lower, k=6)
    u = random.choices(upper, k=4)
    n = random.choices(nums, k=4)
    c = random.choices(characters, k=2)
    medium_password = l + u + n + c
    return medium_password


def get_strong_pw() -> list:
    """generator for strong pw characters

    Returns:
        list: list of output randomly generated characters
    """
    l = random.choices(lower, k=6)
    u = random.choices(upper, k=5)
    n = random.choices(nums, k=5)
    c = random.choices(characters, k=4)
    strong_password = l + u + n + c
    return strong_password


def get_password(input_strength: str) -> bool:
    """pw generator depending on user strength input

    Args:
        input_strength (str): user defined

    Returns:
        bool: validation
    """
    input_strength = input_strength.lower()
    is_valid = input_validation(input_strength)
    if not is_valid:
        print("Password can be either strong, medium or weak. Type again!")
        return False

    if input_strength == pw_strength[0]:
        password = get_weak_pw()
    elif input_strength == pw_strength[1]:
        password = get_medium_pw()
    elif input_strength == pw_strength[2]:
        password = get_strong_pw()

    random.shuffle(password)
    password_final = ''.join(password)
    print(password_final)
    return True


def main():
    """starter for password generator
    """
    while True:
        how_strength = input("How strong do you want your password? weak, medium, strong: ")
        generate_password = get_password(how_strength)
        if not generate_password:
            continue

        break
    print("Note your password somewhere save.")

main()
