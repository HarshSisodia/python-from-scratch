# Shorthand if-else: A one-line way to write a simple if-else statement.
# Result= Value_if_true if condition else value_if_false
#if condition:
    #Result= Value_if_true
#else:
    #Result= Value_if_false
a=500
b=100
print("A") if a>b else print("=") if a==b else print("B")

'''OUTPUT:-
Condition1:- A
Condition2:- B
Condition3:- =
'''


c=9 if a>b else 0
print(c)

#OUTPUT:- 9
