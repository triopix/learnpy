either = float | int


def sum_numbers(*numbers: either) -> either:
    """Returns the sum of multiple numbers

    :param ``numbers``: ``*args`` type argument, specifies multiple numbers
    :return: sum of all numbers
    :rtype: `float` or `int`
    :raises:
       | ``TypeError`` → if any number is not of type ``float`` or ``int``
    """
    # debugging
    #  print(numbers, "\n")
    #  return sum(numbers)
    s: either = 0
    for number in numbers:
        if not isinstance(number, float | int) or isinstance(number, bool):
            raise TypeError("Argument passed must be of type `int`")
        s += number
    return s


sm = sum_numbers(1, 3, 3, 4.0, 5)    # sm = 15
print(type(sm))
print(sm)
