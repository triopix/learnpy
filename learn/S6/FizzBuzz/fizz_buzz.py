import os


def fizz_buzz(x: int) -> str:
    r"""FizzBuzz in Python
==================

    Play FizzBuzz with given value `x`

       * "*fizz*" → if `x` is divisible by ``3``
       * "*buzz*" → if `x` is divisible by ``5``
       * "*fizz buzz*" → if  `x` is divisible by ``3`` **and** ``5``
       * ``str(x)`` → if `x` is divisible by neither ``3`` **nor** ``5``

    :param ``x``: Value to parse such that :math:`\{x \in \ \mathbb{Z}\}`
    :type ``x``: `int`
    :return: Return "*fizz*", "*buzz*", or "*fizz buzz*" depending on `x`
    :rtype: `str`
    :raises:
        ``TypeError`` → if ``type(x)`` is not ``int``
    """
    if not isinstance(x, int):
        raise TypeError("x must be an integer")

    st1 = (x % 3 == 0)
    st2 = (x % 5 == 0)
    st3 = st1 and st2
    st4 = not (st1 or st2)

    if st3:
        return "fizz buzz"
    elif st4:
        return str(x)
    elif st1:
        return "fizz"
    elif st2:
        return "buzz"
    else:
        return str(None)


print(fizz_buzz.__doc__)
print("-" * 80)

# ----------------------------------------------------------------------------------
# for i in range(101):
#     print(fizz_buzz(i))

# game!

while True:
    inp = input("Python FizzBuzz Game: Press ENTER to start: ")
    if inp == "":
        os.system("clear")
        break

k = 0    # counter for player
end = 20    # game length
for i in range(1, end + 1, 2):  # increment every 2, for computer resopnse
    k = i + 1

    print(f"\u001b[35m\u001b[1mComp: \u001b[0m{fizz_buzz(i)}")

    if i == end:
        break

    player_input = input("Your go: ").casefold()  # player's response'

    if player_input != fizz_buzz(k):
        print(f'\u001b[31mYou got it wrong! It was "{fizz_buzz(k)}"')
        break
else:
    # if loop terminates normally {not through a break}
    print("\u001b[32mYay you got all of them!!!")
