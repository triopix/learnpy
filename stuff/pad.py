# delimiters ignored for raw strings
print(r"I love \"stuff\"")

# f string feature

def mySquare(n):
    return n ** 2


print(f'Here is a function call: {mySquare(10)}')


# using \ to split text: outputs as a single line
someText = "This text \
has been split \
over several lines."

print(someText)

# include backslash character in the string (raw string)
someText = r"This text has \ been split \ over \ and over \ again"


# note: strings are immutable, therefore someText is rebounded to a new string
print(someText)
