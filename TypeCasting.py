#TypeCasting
a="1" #String
b="2" #String
print(a+b) #Concatenation of two strings

# c=1 #Integer
# d=2 #Integer
# print(c+d) #Addition of two integers

print(int(a)+int(b)) #Addition of two integers after typecasting


#Exercise :- Explicit Typecasting
String="10" #String
number=7
String_Number=int(String) #Typecasting string to integer

sum = String_Number + number #Addition of two integers after typecasting
print("The sum of both number is " + str(sum)) #Addition of two integers after typecasting


#Exercise :- Implicit Typecasting
a=10 #Integer
print(type(a)) #Type of a is integer
b=2.5 #Float
print(type(b)) #Type of b is float
sum=a+b #Addition of integer and float
print("The sum of both number is " + str(sum)) #Addition of integer and float
print(type(sum)) #Type of sum is float because float has more precision than integer