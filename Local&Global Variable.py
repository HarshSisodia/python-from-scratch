"""Local Variable

A local variable is created inside a function and can only be used within that function. It is destroyed automatically when the function finishes executing.

Easy to remember:
“Inside the function = Local variable.”


Global Variable

A global variable is created outside all functions and can be accessed from anywhere in the program. To modify it inside a function, use the global keyword.

Easy to remember:
“Outside the function = Global variable.”"""


# Code:-

# x=4 #global Variable
# print(x)

# def hello():
    
#     x=5. #local Variable
#     print(f"The local x is {x}")
#     print("Hello World!")

# print(f"The Global x is {x}")
# hello()
# print(f"The Global x is {x}")


x=10
def myfunc():
    global x # Its use to change the global variable value in a function and after that it changeable at global level
    x=4
    y=5
    print(y) 

myfunc()
print(x)
# print(y) :- Its show the NameError bcz is a local variable in a function.



