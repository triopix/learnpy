# mutability check - through id

letters = ["a", "b", "c", "d"]
another_letters = letters

print(letters, "\n", id(letters))

letters+="e"
print(letters, "\n", id(letters)) # same id (mutable)


print(another_letters) # changed
print(id(another_letters))
