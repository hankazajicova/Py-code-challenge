def get_fibonacci(count_numbers: int) -> list:
    """get fibonacci sequence of input count of numbers

    Args:
        count_numbers (int): user input count of numbers

    Returns:
        list: fibonacci sequence
    """
    fibonacci = [0, 1]
    for _ in range(0, count_numbers - 2):
        sum_last_two = sum(fibonacci[-2:])
        fibonacci.append(sum_last_two)

    return fibonacci

numbers = int(input("How many Fibonacci numbers? "))

fibonacci_sequence = get_fibonacci(numbers)
print(fibonacci_sequence)
