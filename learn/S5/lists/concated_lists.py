empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

numbers = [even, odd]
print(numbers)

print("-"*80)

for number_list in numbers:
    # print each value
    for value in number_list:
        print(value)
        
