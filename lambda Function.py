#Lambda Function (One-line Statement):
#A lambda function is a small anonymous function in Python used to create a function in a single line using the lambda keyword.

# def double(x):
#     return x*2

#lambda arguments: expression
double=lambda x: x*2
cube=lambda x: x*x*x
avg=lambda x,y,z: (x+y+z)/3
print(double(5))
print(cube(5))
print(avg(5, 10,15))

#we also the function which mean we can pass the lambda function as an argument to another function.
# def appl(fx,value):
#     return 6+ fx(value)

# print(appl(cube,2))

def appl(fx,value):
    return 6+ fx(value)

print(appl(lambda x: x*x,2))

'''
OUTPUT:- 
10
125
10.0
10
'''
