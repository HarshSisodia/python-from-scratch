age=int(input("Enter your age: "))
print("Your Age is", age)

#Condition Operators
# <, >, <=, >=, ==, !=
# print(age>18)
# print(age>=18)
# print(age!=18)

#if - else:
if(age>=18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

'''OUTPUT:
Enter your age: 89
Your Age is 89
You are eligible to vote.'''



#if-elseif-else:

num=int(input("Enter your Number: "))

if num<0:
    print("Its a Negitive Number")
elif num==0:
    print("Its a Neutral Number")
elif num==999:
    print("NUmber is Unique")
else:
    print("Its a positive Number")

a="i am happy now"
print(a.capitalize())

'''
OUTPUT:
Enter your Number: -1
Its a Negitive Number

Enter your Number: 0
Its a Neutral Number

Enter your Number: 999
NUmber is Unique
I am happy now

Enter your Number: 98
Its a positive Number
'''


#Nested if statement

num1= int(input("Enter your Number: "))
print("Your Number is:", num1)

if num1<0:
    print("Its Negitive")
elif(num1>0):
    if num1<=10:
        print("Number between 1-10")
    elif( num1 >10 and num1 <=20):
        print("Number is between 11-20")
    else:
        print("Number is greater then 20")
else:
    print( "Its Zero")

''''
OUTPUT:
Enter your Number: 0
Your Number is: 0
Its Zero

Enter your Number: 45
Your Number is: 45
Number is greater then 20

Enter your Number: -1
Your Number is: -1
Its Negitive

Enter your Number: 12
Your Number is: 12
Number is between 11-20
'''
