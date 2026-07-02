#Break Statement
a=int(input("Enter a number: "))
for i in range (1,101,1):
    print(i, end=", ")
    if i==a:
        if(i%2==0):
            print("\nThe number is Even\n")
            break
        else:
            print("\nThe number is Odd\n")
            break

''' Output:
Enter a number: 23
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
The number is Odd


Enter a number: 24
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
The number is Even

'''


#Continue Statement
a=int(input("Enter a number: "))
for i in range (1,50,1):
    
    if i==a:
        if(i%2==0):
            print("Number is a even number so its skipped")
            continue
        

        else:  
           print("Number is a odd number so its skipped")
           continue
    print(i, end=", ")


    ''' Output:
    Enter a number: 10
1, 2, 3, 4, 5, 6, 7, 8, 9, Number is a even number so its skipped
11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, %         

    Enter a number: 11
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, Number is a odd number so its skipped
12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, %
  
    '''
       
           