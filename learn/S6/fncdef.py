# pass by reference behaviour, changes ORIGINAL VARIABLE!!!
def change_x(x: list) -> list:
    x.pop()
    return x


a = [1, 2, 3]
print(f"Function Applied -> {change_x(a)}")

# ORIGINAL list changed!
print(f"Original List (modified) -> {a}")

print("="*39)
# -------------------------------------------------------------------------------------

# To solve, pass a copy of the mutable type
o = [1, 3, 5]
print(f"Function Applied to copy of list -> {change_x(o.copy())}")

# list unchanged!
print(f"Original List (unmodified) -> {o}")

print("="*39)
# ------------------------------------------------------------------------------------

# pass by value behaviour - does not change original variable


def change_b(b: int) -> int:
    b -= 1
    return b


k = 2
print(f"Change variable -> {change_b(k)}")

# original kept!
print(f"Original Variable value -> {k}")
