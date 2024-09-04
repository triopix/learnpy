import math as m

for i in range(1, 13):
    # field width {expression:#} -> # = {1, 2, 3, 4 ...} (default left justified)
    print(f"No. {i:2} squared is {(i ** 2):<5} and cubed is {(i ** 3):^2}")

    # {exp:<#} formats right justifies #. of times
    # {exp:^#} center formats #. of times

print()


print(f"1. Pi is approximately {(m.pi):.48f}") # max digit precision = 48
 

# No 'f' at end? Example: 3.1232 will get rounded to 3.123
print(f"2. Pi is approximately {(m.pi):70.50f}") 
print(f"3. Pi is approximately {(m.pi):30.28f}") # 28 decimals + the 3 and the dot = 30 field width
print(f"4. Pi is approximately {(m.pi):30.48f}") # overrides field width

print(f"5. Pi is approx {(m.pi):.48f}")

# field number is optional!