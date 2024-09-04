activity = input("Where do you want to go today?: ")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema!")
else:
    print("Yay! Let's go")

# use casefold instead of lowercase
# string methods: https://www.w3schools.com/python/python_ref_string.asp
# docs.python.org: https://docs.python.org/3/library/stdtypes.html
    