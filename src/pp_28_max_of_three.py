ONE = 1
TWO = 2
THREE = 3

def get_max(var1: int, var2: int, var3: int) -> int:
    """find the max muber without max()

    Args:
        var1 (int): input variable 1
        var2 (int): input variable 2
        var3 (int): input variable 3

    Returns:
        int: max value
    """
    max_var = var2
    if max_var < var1:
        max_var = var1

    if max_var < var3:
        max_var = var3

    print("max number is: {max}".format(max=max_var))
    return max_var

maximum = get_max(ONE, TWO, THREE)
print(maximum)
