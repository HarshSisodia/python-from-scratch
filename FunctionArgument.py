#Default Argument :
def average(a=9,b=1): #Function with default argument
    print("The average of two numbers is: ", (a+b)/2)
#average(10,20) #Calling the function with two arguments
average()
# average(10) #Calling the function with one argument
average(b=20) #Calling the function with one argument

'''
OUTPUT:
The average of two numbers is:  15.0
The average of two numbers is:  5.0
The average of two numbers is:  5.5
The average of two numbers is:  14.5
'''


#Keyword Argument :
def average(a,b): #Function with keyword argument
    print("The average of two numbers is: ", (a+b)/2)
average(b=20,a=10) #Calling the function with keyword arguments
'''
OUTPUT:
The average of two numbers is:  15.0
'''

#Required Argument : 
def name(fname,mname,lname="waston"): #Function with required argument
    print("The name is: ", fname, mname, lname)

name("Harry", "Potter") #Calling the function with two required arguments

'''
OUTPUT: The name is:  Harry Potter waston
'''


#Variable Length Argument :
def average(*numbers): #Function with variable length argument
    print(type(numbers)) #it will print the type of the variable numbers which is tuple.
    sum=0
    for i in numbers:
        sum+=i
    # print("The average of the numbers is: ", sum/len(numbers))
    return sum/len(numbers)
c= average(10,20,30,40,50) #Calling the function with variable length argument
print("The average of the numbers is: ", c)
average(10,20) #Calling the function with variable length argument

'''
OUTPUT:
The average of the numbers is:  30.0
<class 'tuple'>
The average of the numbers is:  15.0
ass 'tuple'>
The average of the numbers is:  30.0 #when we usereturn statement in the function
'''


#keyword arbitrary argument : Dictionary
def name(**names): #Function with keyword arbitrary argument
    print(type(names)) #it will print the type of the variable names which is dictionary.
    print("Hello", names["fname"], names["mname"], names["lname"], names["Nature"])

name(fname="Harry", mname="James", lname="Potter", Nature="is a Soft hearted person") #Calling the function with keyword arbitrary argument

'''OUTPUT:
<class 'dict'>
Hello Harry James Potter  is a Soft hearted person
'''
