#Recursion:- It is the process of defining something in terms of itself.
#factrial(7)=7*6*5*4*3*2*1

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return(n*factorial(n-1))

n=5
print("Number: ", n)
print("factorial is: ", factorial(n))

'''Output:
Number:  5
factorial is:  120

Dry Run:-
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1
'''



#Fibonacci Sequence:-
'''
f(0)=0
f(1)=1
f(2)=f(0)+f(2)
f(n)=f(n-1)+f(n-2)
0 1 1 2 3 5 8....
'''

def fibbo(num):
    if(num==0 or num==1):
        return 1
    else:
        return(fibbo(num-1)+fibbo(num-2))
num=6
print("Fibbo Number: ", num)
print("Fibbo of num is : ", fibbo(num))

'''
Output:- 
Fibbo Number:  6
Fibbo of num is :  13
'''