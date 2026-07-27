#The import keyword is used to bring an entire module into your Python program. It allows you to use the functions, classes, and variables defined inside that module without writing the code yourself.
# import math
# result=math.sqrt(9)
# print(result)

#The from keyword is used to import only the specific function, class, or variable you need from a module. This lets you use it directly without writing the module name every time.
# from math import sqrt,pi
# result=sqrt(9) *pi
# print(result)

#The from module_name import * statement imports all public functions, classes, and variables from a module into your program. After importing, you can use them directly without writing the module name.
#from keyword is use to 
# from math import *
# a=sqrt(8)* pi
# print(a)

#Use as for short import math and it is easy to access a long module in a short form
# import math as m
# result=m.sqrt(7)
# print(result)

#The dir() function is used to display a list of all the attributes, methods, and functions available in an object or module. It is mainly used to explore what operations you can perform on a particular object.
# import math
# print(dir(math))


# If you create a function in another .py file, you can use the from ... import statement to import that function into your current Python file. This helps you reuse code instead of writing the same function again.
# math_operations.py
# def add(a, b):
#     return a + b

# main.py
# from math_operations import add

# result = add(10, 20)
# print(result)
'''
OUTPUT:-
3.0
9.42477796076938
8.885765876316732
2.6457513110645907

['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh','atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 
'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 
'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
'''