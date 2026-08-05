#is:-    is (Identity Operator): Checks whether two variables refer to the same object in memory. It returns True if both variables point to the same object; otherwise, it returns False. 
# Its give a exact location of the object in memory. It is used to compare the memory locations of two objects.


#==:- == (Equality Operator): Checks whether the values of two objects are equal. It returns True if the values are the same; otherwise, it returns False. 
# Its give a exact value of the object in memory. It is used to compare the values of two objects.

a=[1,2,3]
b=[1,2,3]
print(a is b)  # Output: False (Different objects in memory)
print(a == b)  # Output: True (Same values)

c=3
d=3
print(c is d)  # Output: True (Same object in memory for small integers)
print(c == d)  # Output: True (Same values)

e="Lion"
f="Lion"
print(e is f)  # Output: True (Same object in memory for strings)
print(e == f)  # Output: True (Same values)

g=None
h=None
print(g is None)  # Output: True (Both refer to the same None object)  
print(g == h)  # Output: True (Both are None, so they are equal)