#Raising custom error:-
a=int(input("Enter the value between 5 and 9: "))

if a<5 or a>9:
    raise ValueError("Enter valid Number which is lie between 5 and 9")


#Quick QUIZ:-

b=input("Enter the String: ")
if b=="quit":
    print("Workable")
else:
    raise KeyboardInterrupt("Our Input b is not equal with quit")

'''
OUTPUT:-
Enter the value between 5 and 9: 2
Traceback (most recent call last):
  File "/Users/harshsisodia/Desktop/python from scratch /CustomError.py", line 4, in <module>
    raise ValueError("Enter valid Number which is lie between 5 and 9")
ValueError: Enter valid Number which is lie between 5 and 9

#QUICK QUIZ:-
Enter the String: harry
Traceback (most recent call last):
  File "/Users/harshsisodia/Desktop/python from scratch /CustomError.py", line 14, in <module>
    raise KeyboardInterrupt("Our Input b is not equal with quit")
KeyboardInterrupt: Our Input b is not equal with quit
'''