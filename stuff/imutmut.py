# mutable vs immutable types

"""
    
    str
    int 
    float
    bool
    byte
    tuple
    
    mutable:
    
    list 
    set 
    dict
    
    other 3rd party library types
    """ 

x = "hello"
y = x # makes a real copy 

print(x, y)

x = "mom" # reassigning new value to x
print(x, y)

y = "something" # doesn't change x in any way
print(x, y)

x = y
y = x
print(x, y)

z = [1, 2, 3]
v = z
z[0] = 2
print(z, v) # changes for v because it is an alias