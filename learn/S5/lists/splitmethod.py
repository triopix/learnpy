"""

.split() always returns -> a list of strings or chars - requires a seperator already present in string 
.join() - adding a seperator at every ধাপ -> returns a string

"""

pangram = """The quick brown fox
\t jumps over 
the lazy dog"""

# defaults to splitting on whitespace
words = pangram.split()
print(words)
print(type(words))

numbers = "9223445334242903"
numbers = ",".join(numbers) 
print(numbers)
print(type(numbers))

after = numbers.split(',')
print(after)
print(type(after))


values = [int(x) for x in after]
print(values)
print(type(values))
print(type(values[0])) # int


print("="*80)


def insert_separator(string, separator, n):
    # Handle edge cases
    if not string:
        return ""
    if n <= 0:
        raise ValueError("Chunk size 'n' must be greater than 0.")

    # Create chunks of the string with length n
    chunks = [string[i:i+n] for i in range(0, len(string), n)]
    # Join chunks with the separator
    return separator.join(chunks)


# Example usage
numbers = "9223445334242903"
n = 2
separator = ","

formatted_numbers = insert_separator(numbers, separator, n)
print(formatted_numbers)

# Testing edge cases
empty_string = ""
formatted_empty = insert_separator(empty_string, separator, n)
print(f"Formatted empty string: '{formatted_empty}'")

# Testing invalid n
try:
    formatted_invalid_n = insert_separator(numbers, separator, 0)
except ValueError as e:
    print(e)


# trying to get "9223445334242903" - overloading not supported anyway

def format_number(string, separator, n):
    # Handle edge cases
    if not string:
        return ""
    if n <= 0:
        raise ValueError("Chunk size 'n' must be greater than 0.")

    rev = string[::-1]

    # Create chunks of the string with length n
    chunks = [rev[i:i+n] for i in range(0, len(string), n)]

    joined_chunks = separator.join(chunks)

    formatted_string = joined_chunks[::-1]

    # Join chunks with the separator
    return formatted_string

changed_numbers = format_number(numbers, ',', 3)
print(changed_numbers)
