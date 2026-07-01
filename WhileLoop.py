i=0
while(i<3):
    print(i)
    i=i+1

''' Output:
0,1,2
or if we do i<=3 then the output will be 0,1,2,3
'''


#Decrementing while loop
count=5
while(count>0):
    print(count, end=", ")
    count-=1
else:
    print("The number is less than or equal to 0\n")

''' Output:5, 4, 3, 2, 1, % '''



#new Code

j= int(input("\nEnter the Number:\n"))
while(j<=20):
    j=int(input("\nEnter the Number:\n"))
    print(j, end=", ")
    if j<0:
       print("\nThe number is Negitive\n") 
       
print("\nThe number is greater than 20\n")



#How to emulate a do while loop in python
while True:
    num=int(input("Enter the number: "))

    if num>10:
     break
