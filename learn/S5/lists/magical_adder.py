# string input
values = "".join(input("Please enter three numbers: ")).split(",")

"""

1. joining inputs into a string
2. Splitting that string into parts using seperator - converts into list

"""

# int values
integer_values = [int(x) for x in values]

# assign letters to values - nifty trick ;)
a, b, c = integer_values

# print result
print(a + b - c)
