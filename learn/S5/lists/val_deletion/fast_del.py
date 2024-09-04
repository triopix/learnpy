import random as rand

min_valid = 400
max_valid = 800
elements = 10
breaker = "-" * 80
breaker2 = "=" * 80

# Initialize list
my_list = [rand.randint(1, 1000) for _ in range(elements)]

# Create copies of the list
dup_list = my_list.copy()
my_sorted_list = sorted(my_list)

print(f"Original List: {my_list}")
print(f"Sorted List: {my_sorted_list}\n")
print(breaker)

# Reverse Indexing Method for unsorted list
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] < min_valid or my_list[i] > max_valid:
        del my_list[i]

print(f"Modified Original List (Reverse Indexing Method): {my_list}")

# Optimized sorted list deletion
low_index = next(
    (i for i, v in enumerate(my_sorted_list) if v >= min_valid), len(my_sorted_list)
)
high_index = next(
    (i for i, v in enumerate(my_sorted_list) if v > max_valid), len(my_sorted_list)
)

del my_sorted_list[:low_index]
del my_sorted_list[high_index - low_index:]

print(f"Final Modified Sorted List: {my_sorted_list}")
