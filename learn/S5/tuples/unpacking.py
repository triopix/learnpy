# unpacking tuples

a = b = c = d = e = f = 13
print(c)

print("Unpacking a tuple: ")

data = (1, 2, 76)  # tuple
print(data)
# each variable assigned to data[i]
# you can't have a tuple on left hand side - because they are immutable
x, y, z = data
print(x, y, z)


print("Unpacking a list")


data_list = [12, 13, 4]
print(data_list)
# appending another item will make it crash
# data_list.append(10)

p, q, r = data_list
print(p, q, r)

# tuples can be unpacked succesfully and safely


