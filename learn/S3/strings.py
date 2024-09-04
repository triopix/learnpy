text = "Norwegian Blue"

index = 10
neg_index = index - len(text) # 3 - 14 = -11

print(neg_index)
print(text[neg_index])

# python idioms
print(text[::-1]) # reverse
print(text[:]) # whole str
print(text[:-1]) # last char

print(text[:index] + text[index:]) # whole string


letters = "abcdefghijklmnopqrstuvwxyz"

print(letters.index('o'))
print(letters[-6:1:-1])
print(letters[-10:-13:-1]) # without adding -1, python can't tell which way you want to go
print(letters[4::-1])

# important
print(letters[:17:-1]) 
print(letters[17::-1]) 
print(letters[:16:-1]) 
print(letters[-5:]) # slice forward NOT backward because no -1 step defined
print(letters[-5::-1]) # go backwards

# empty string
letters = ""
print(letters[:1]) # useful for getting first item without code crashing (no need to use try and catch)
# print(letters[0]) # returns error if the string is empty

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"

# letters in reverse order
print(data[-1::-5])


# letters in forward order
print(data[2::5])

# getting numbers in reverse order
print((data[::5])[::-1]) # getting 12345678 and then reversing it

# or you can do this
print(data[-3::-5])

# what does this do?
print(data[:-1:5]) # starting from the start and ending not including -1

# what about this?
print(len(data))
negIndex = (0 - len(data))
print(negIndex) # equivalent to 0 in forward mode

# getting the colons
print(data[-2:negIndex:-5])
print(data[-2::-5])
print(data[-2:-38:-5])