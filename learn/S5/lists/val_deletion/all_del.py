import random as rand

min_valid = 400
max_valid = 800
elements = 10

breaker = "-" * 80
breaker2 = "=" * 80

# intialize list
my_list = []

# add elements to list
for i in range(elements):
    my_list.append(rand.randint(1, 1000))

# my_list[:] original unchanged, regardless of modifications made
dup_list = my_list.copy()
my_sorted_list = sorted(my_list)  # sorted list

print(f"Original List: {my_list}")
print(f"Sorted List: {my_sorted_list}\n")

print(breaker)
# iterate backwards to remove rogue values
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] < min_valid or my_list[i] > max_valid:
        del my_list[i]

print(f"Modified Original List (Reverse Indexing Method): {my_list}")

# reinstating my_list
my_list = dup_list.copy()

# iterate over my_list[:] method
for value in my_list[:]:
    if value < min_valid or value > max_valid:
        my_list.remove(value)

print(f"Modified Original List (Copy Method): {my_list}")

my_list = dup_list.copy()

# reversed iterator method
reversed_list = reversed(my_list)

for value in reversed_list:
    if value < min_valid or value > max_valid:
        my_list.remove(value)

print(f"Modified Original List (Reversed Iterator Method): {my_list}")
print(breaker, "\n")

print("Deleting items from sorted Lists")
print(breaker2)

# sorted lists
index = 0
for value in my_sorted_list:
    if value > min_valid:
        index = my_sorted_list.index(
            value
        )  # delete up to but not including the index value!
        break

print(f"Low value(s) to delete -> index #{index}, for {my_sorted_list}")

# delete until min starts
del my_sorted_list[:index]

print(f"After Low value(s) deleted list {my_sorted_list}")

# delete the high values
for value in reversed(my_sorted_list):
    if value < max_valid:
        index = my_sorted_list.index(value)
        break

print(f"High value(s) to delete -> index #{index}, for {my_sorted_list}")

del my_sorted_list[:index:-1]

print(f"After High value(s) deleted list {my_sorted_list}")

print(f"Final Modified Sorted List: {my_sorted_list}")
