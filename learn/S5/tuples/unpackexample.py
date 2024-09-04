# only using one variable
for t in enumerate("abcdefgh"):
    #  (index, char) = (t) - tuples have parentheses, not necessary always
    index, char = (t)
    print(index, char)

# prints a tuple


"""What does this mean!!!"""

# for index, value in enumerate("abcdefgh")

# enumerate returns a tuple for each exmaple
index, character = (0, "a")

print(f"{index}\n{character}")
