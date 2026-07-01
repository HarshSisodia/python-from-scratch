#match statement 
x= int(input("Enter your Number: "))

match x:
    case 0:
        print("Its Zero")

    case 1:
        print("Its One")

    case x if x%2==0 and 0<x<=20:
        print("Its a even Number")

    case x if x%2!=0 and 0<x<=20:
        print("Its a odd Number")

    case _ if 0<x<=50:
        print("Its a positive Number")

    case _ if -50<=x<0:
        print("Its a Negative Number")

    case _ : #it is default case if all the above cases are false
        print(x)