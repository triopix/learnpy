import random as rnd

# see PEP257 for documentation rules 
def get_integer(prompt: str) -> int:
    """ Gets an integer from standard input

    The function will continue looping, and prompting the user until a valid `int` is
    entered.

    :param prompt: The string that the user will see when they're prompted to enter the value
    :type prompt: `str`
    :return: The integer that the user enters
    :rtype: `int`
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("Invalid value entered")
    
# docstring typing
# print(input.__doc__)
# print("*"*80)
# print(get_integer.__doc__)
# print("*"*80)

# help(get_integer)     # gets the documentation for the function


print("Please enter a number bewteen 1-1000")
highest = 1000
answer = rnd.randint(1, 1000) 
print(answer) # TODO: Remove after testing
guess = 0 # initialize to any number that doesn't equal the answer

while True:
    number = get_integer(": ")
    
    if number == 0:
        break
    if number > answer:
        print("Please guess lower\n")
    elif number < answer: 
        print("Please guess lower\n")
        
    if number == answer:
        print("Congrats you guessed it!")
        break
