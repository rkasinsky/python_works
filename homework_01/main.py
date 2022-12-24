"""
Домашнее задание №1
Функции и структуры данных
"""
import platform


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    result = []
    for item in args:
        result.append(item ** 2)
    return result


numbers = [1, 2, 3, 4, 5, 6, 7]
assert power_numbers(1, 2, 3, 4, 5, 6, 7) == [1, 4, 9, 16, 25, 36, 49]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number: int):
    if int(platform.python_version().split(".")[1]) > 10:
        number = number * -1 if number < 0 else number
    else:
        if number < 0:
            number = number * -1

    d = 2

    if number > 1:
        while number % d != 0:
            d += 1
    else:
        d = number + 1
    return d == number


assert is_prime(131)
assert not is_prime(10)


def filter_numbers(numbers_in_filter: list, filter_type: str):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    result = []
    fail_message = f'Wrong filter type: use "{ODD}", "{EVEN}" or "{PRIME}"'

    print(f"Start check: numbers = {numbers_in_filter}, type = {filter_type}")

    if filter_type == ODD:
        print(f'Got {ODD} filter type')
        result = list(filter(lambda p: p % 2 != 0, numbers_in_filter))
    elif filter_type == EVEN:
        print(f'Got {EVEN} filter type')
        result = list(filter(lambda p: p % 2 == 0, numbers_in_filter))
    elif filter_type == PRIME:
        print(f'Got {PRIME} filter type')
        result = list(filter(is_prime, numbers_in_filter))
    else:
        pass
    return result if result else fail_message


assert filter_numbers(numbers, EVEN) == [2, 4, 6]
assert filter_numbers(numbers, ODD) == [1, 3, 5, 7]
assert filter_numbers(numbers, PRIME) == [2, 3, 5, 7]
