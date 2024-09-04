Fibonacci sequence in Python
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
