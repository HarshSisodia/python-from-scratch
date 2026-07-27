#The if __name__ == "__main__": statement is used to execute a block of code only when the Python file is run directly.
#  If the file is imported into another Python file, the code inside this block does not execute.
'''
* To prevent test code or demo code from running when the file is imported.
* To make a Python file reusable as a module.

 math_operations.py:-
 def add(a, b):
    return a + b

print("This line always runs.")

if __name__ == "__main__":
    print("This file is running directly.")
    print(add(10, 20))

main.py:-
from math_operations import add

result = add(5, 7)
print(result)

OUTPUT:-
This line always runs.
This file is running directly.
30
'''

def main():
    print("Welcome to python")

if __name__ == "__main__":
    main()

# OUTPUT:- Welcome to python