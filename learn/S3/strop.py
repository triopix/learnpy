"""

A sequence is defined as an ordered set of items. 

Sequence types in python: You can use indexing to get individual items

- List
- String
- Tuples
- Bytes/Bytearrays

Not all sequence types can be concatenated or multiplied. Range is an example
that cannot be concatenated

"""

string1 = "he's"
string2 = " spining"
print(string1 + string2)

print("Hello" " World")

print("hello" * 5 + str(4))
print("Hello" * (5 + 4))

today = "friday"
print("day" in today) # True
print("fri" in today) # True
