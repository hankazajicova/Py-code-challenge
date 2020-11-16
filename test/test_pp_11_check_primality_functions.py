from src.pp_11_check_primality_functions import is_prime, get_divisors


def test_is_prime():
    """tests the is_prime method for True
    """
    # arrange
    divisors = [1, 5]
    expected = True

    #act
    result = is_prime(divisors)

    #assert
    assert result == expected


def test_is_prime_not_prime():
    """tests the is_prime method for False
    """
    # arrange
    divisors = [1, 5, 10, 15]
    expected = False

    #act
    result = is_prime(divisors)

    #assert
    assert result == expected


def test_get_divisors():
    """tests the get_divisors methond
    """
    input_number = 10
    expected = [1, 2, 5, 10]

    result = get_divisors(input_number)

    assert result == expected
