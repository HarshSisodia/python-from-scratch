def square(n):
    '''This is n use for input and function can be make for squaring of any number.'''
    print(n**2)
square(5)
print(square.__doc__) 

# Output:- 25
# This is n use for input and function can be make for squaring of any number.


#if we write the print(n) or anything just below the function so it is not print the docstring.
def cube(n):
    print(n)
    '''This is n use for input and function can be make for cubing of any number.'''
    print(n**3)
cube(5)
print(cube.__doc__) 

# #Output:5
# 125
# None



##PEP-8:- Program Enhancement Porposal :- It is a document to provide the guideline and best practice on how to write a code and python program should be maintainable, readeable , consisitable.


#The zen of python
import this #Byusing this a ester and zen of python poem should be print and it is related with when we do make a project.

'''Output:
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

