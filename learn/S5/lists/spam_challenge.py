# print all list items with spam remved

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# [:] using a copy
for meal in menu:
    for item in meal[:]:
        if item == "spam":
            meal.remove("spam")
            
    print(', '.join(meal))

# # second solution using reversed iterator (doesn't create a new list)
# for meal in menu:
#     for item in reversed(meal):
#         if item == "spam":
#             meal.remove("spam")
#     print(meal)
