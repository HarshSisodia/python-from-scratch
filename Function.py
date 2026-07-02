#Function is a block of code that is designed to perform a specific task whenever is called.
a=int(input("Enter a First number: "))
b=int(input("Enter a Second number: "))
c=int(input("Enter a Third number: "))
d=int(input("Enter a Fourth number: "))
def CalculateGmean(a,b): #Function to calculate Geometric Mean
    mean=(a*b)/(a+b)
    print(mean)


def IsGreater(a,b): #Function to check which number is greater
    if a>b:
        print("The First number is greater than Second number")
    elif a<b:
        print("The Second number is greater than First number")
    else:
        print("Both numbers are equal")


def IsLesser(a,b):
    pass   #it is used to indicate that the function is not yet implemented and will be implemented in the future.

CalculateGmean(a, b)
CalculateGmean(c, d)
IsGreater(a, b)
IsGreater(c, d)

'''
OUTPUT:
Enter a First number: 12
Enter a Second number: 1
Enter a Third number: 3
Enter a Fourth number: 4
0.9230769230769231
1.7142857142857142
The First number is greater than Second number
The Second number is greater than First number
'''