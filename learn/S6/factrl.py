# you can do it iteratively or recursively


# https://www.youtube.com/watch?v=DUC1qg7ZaRg
# FOR UNDERSTANDING THE RECURSIVE APPROACH

def factorial(n: int, use_recursive=True) -> int:
    r"""Factorial in Python
===================

    Compute the factorial for given **positive** integer `n`

    The factorial of a number denoted by `n`!
    is the **product** of all the numbers
    from 1 to `n` **inclusive**

    Thus, 4! represents:

       `4 * 3 * 2 * 1 = 24`

    0! returns 1, as per the convention for an empty product

    With the recursive approach, big numbers might result in stack overflow

    :param ``n``: a positive integer
    :param ``use_recursive``: Defaults to ``True`` -> uses recursive approach
       instead of iterative approach
    :return: Returns the product of `n`!
    :rtype: `int`
    :raises:
       | ``ValueError`` → if ``n < 0``
       | ``TypeError`` → if ``type(n)`` is not ``int``
       | ``Recursion Error`` → if max recursion depth reached
    """
    if use_recursive is True:
        if type(n) is not int:
            raise TypeError("n must be a positive integer value")
        elif n < 0:
            raise ValueError("n cannot be less than 0")
        elif n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    else:
        if type(n) is not int:
            raise TypeError("n must be a positive integer value")
        elif n < 0:
            raise ValueError("n cannot be less than 0")
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(n, 0, -1):
                result *= i
            return result
        # {only valid for 9 to 998 - otherwise stack overflow}


print(factorial.__doc__)
print(factorial(1000, use_recursive=True))
