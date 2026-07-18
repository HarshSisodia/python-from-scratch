# Exception Handling: Handles runtime errors to prevent the program from crashing.
# Exception Handling: Used to handle errors and keep the program running.
a=input("Enter the Number: ")
print(f"Multiplication of {a} is: ")

try:
    for i in range(1,11):
     print(f"{a} X {i} = {int(a) * i}")
except:
   print("Invalid Input!")

print("Some Imp Lines Of Code")
print("End of program")

#We can Handle multiple error in single try and exception
try:
   num=int(input("Enter the Integer: "))
   a=[4,3]
   print(a[num])
except ValueError:
   print("Number Entered is not a integer")
except IndexError:
   print("IndexError!")


'''
OUTPUT:-
Enter the Number: 3
Multiplication of 3 is: 
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
3 X 10 = 30
Some Imp Lines Of Code
End of program
Enter the Integer: jfj
Number Entered is not a integer

Enter the Integer: 2
IndexError!

'''