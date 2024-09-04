Factorial in Python
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
:param ``use_recursive``: Defaults to ``True`` → uses recursive approach
   instead of iterative approach
:return: Returns the product of `n`!
:rtype: `int`
:raises:
   | ``ValueError`` → if ``n < 0``
   | ``TypeError`` → if ``type(n)`` is not ``int``
   | ``Recursion Error`` → if max recursion depth reached