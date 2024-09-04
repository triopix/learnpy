working_age = range(16, 65)

print("Please enter your age: ")
age = int(input())

if age in working_age:
    print("Have a good day at work!")
else:
    print("Go home lol!")