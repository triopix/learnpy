# removing items from a list

even = [
    4,
    6,
    8,
    2,
]

odd = [
    1, 
    5, 
    7, 
    3, 
    9
]


# does not create a copy - sorts in place .sort() (rearranges)

print(even)
print(odd)

even.sort() # list itself is modified
print(even)

even.sort(reverse=True)
print(even)


# case insensitive sorting
print(sorted("The quick brown fox jumps over the lazy dog", key=str.casefold))
