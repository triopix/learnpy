FizzBuzz in Python 
==================

Play FizzBuzz with given value `x`

   * "*fizz*" → if `x` is divisible by ``3``
   * "*buzz*" → if `x` is divisible by ``5``
   * "*fizz buzz*" → if `x` is divisible by ``3`` **and** ``5``
   * ``str(x)`` → if `x` is divisible by neither ``3`` **nor** ``5``

:param ``x``: Value to parse such that :math:`\{x \in \ \mathbb{Z}\}`
:type ``x``: `int`
:return: Return "*fizz*", "*buzz*", or "*fizz buzz*" depending on `x`
:rtype: `str`
:raises:
    ``TypeError`` → if ``type(x)`` is not ``int``