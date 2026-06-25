#Variable
a=1 #Integer
print(a)
b=True #Boolean
print(b)
c="Hello Learner" #String
print(c)
d=None #Data Types
print(d)
e=1.5 #Float
print(e)

f=complex(1,2) #Complex
print(f)


#DataTypes
print("The type of a is:", type(a))
print("The type of b is:", type(b))
print("The type of c is:", type(c))
print("The type of d is:", type(d))


#List :- its a collection of items in a particular order. 
# It is mutable, meaning you can change its content without changing its identity. 
# Lists are defined by having values between square brackets [ ].
my_list=[[1,2,3,4,5],1.1,True,"Hello Learner"]
print(my_list)

#tuple :- its a collection of items in a particular order. 
# It is immutable, meaning you cannot change its content without changing its identity.
# Tuples are defined by having values between parentheses ( ).
my_tuple=((1,2,3,4,5),("Hello Learner","World"),(False),1.1)
print(my_tuple)


#dictionary :- its a collection of items in a particular order.
# It is mutable, meaning you can change its content without changing its identity.
# Dictionaries are defined by having values between curly brackets { }.
my_dict={"Name":"Harsh","Age":20,"Course":"Python"}
print(my_dict)


"""1
True
Hello Learner
None
1.5
(1+2j)
The type of a is: <class 'int'>
The type of b is: <class 'bool'>
The type of c is: <class 'str'>
The type of d is: <class 'NoneType'>
[[1, 2, 3, 4, 5], 1.1, True, 'Hello Learner']
((1, 2, 3, 4, 5), ('Hello Learner', 'World'), False, 1.1)
{'Name': 'Harsh', 'Age': 20, 'Course': 'Python'}"""
