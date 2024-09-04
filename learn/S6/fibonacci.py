# Refer to 7.2.5 - economy of expresssion
# For the lay man, this documentation would suffice
# Unless a programmer reads this, they would know what fibonacci already is
# and the documentation would be too verbose

# INFO: Recursion in place becomes inefficient for very large numbers

def fibonacci(n: int) -> tuple:
    r"""Fibonacci sequence in Python
============================

    Generate a Fibonacci sequence of size `n` (*#. of terms*)

    Through subscript notation :math:`F_{n}` we can define:

       :math:`F_{n = 0} = 0` and :math:`F_{n = 1} = 1`

    and the recursive function:

       :math:`F_{n} = F_{n-1} + F_{n-2} \to \{n\in \mathbb{N}, n>1\}`

    Where each subsequent term :math:`F_{n}` is produced from the
    **sum** of the previous two terms :math:`F_{n-1}` and :math:`F_{n-2}`
    in the sequence.

    **Refer to**: https://en.wikipedia.org/wiki/Fibonacci_sequence

    :param ``n``: number of terms in the sequence
    :type ``n``: `int`
    :return: Return a **Fibonacci sequence** containing the elements up to `n`
    :rtype: `tuple`
    :raises:
       ``ValueError`` → if ``n < 1``
    """
    if n < 1:
        raise ValueError("Invalid argument. n must be greater than 1")

    # logic
    fib = [0, 1]    # predefined values, *check docs*
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return tuple(fib)


docs = fibonacci.__doc__    # print documentation
print(docs, "\n")

n = int(input())   # number of terms

example = fibonacci(n)    # (0, 1, ...)`    `
print(example)


# Generate fibonacci number at certain index

def get_fibonacci(index: int):
    """Return the fibonacci number at given positive integer: `index`"""
    # 0th, 1st = 0, 1
    a, b = 0, 1
    result = None
    for _ in range(index - 1):
        result = a + b    # get the next term
        # shift indicies to add the previous term + result
        a = b
        b = result
    return result


k = int(input())

print(get_fibonacci(k))    # (0, 1, 1, 2, 3, 5) -> index: 5, value: 5
