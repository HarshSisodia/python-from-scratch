#Finally keyword is apart of exception handling which is used to always execute the code. Below is a example:
#Also we use finally keyword in a function
def func():
    try:
        li=[1,2,4,6]
        a=int(input("Enter the Index: "))
        print(li[a])
        return 1
    except:
        print("Some Error Occured!")
        return 0

    finally:
        print("Code always be Executed")

    # print("Code always be Executed")


x=func()
print(x)
'''
OUTPUT:-
Enter the Index: 1
2
Code always be Executed

Enter the Index: 4
Some Error Occured!
Code always be Executed


Enter the Index: 1
2
Code always be Executed
1

Enter the Index: 4
Some Error Occured!
Code always be Executed
0
'''