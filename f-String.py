#f-string:-
val="hey my name is {} and I am from {}"
name="Harsh"
Country="India"
print(val.format(name,Country)) # Output:- hey my name is Harsh and I am from India
# print(val.format(Country, name)) #Output:- when we write the val like val="hey my name is {1} and I am from {0}" then output is hey my name is Harsh and I am from India.
Price=49.0999
txt=f"The price {Price:.2f} of Orange"
#print(txt.format(Price=49.0999)) #its print 2 decimel value of after point(Output:-The price  49.10 of Orange)
print(txt) #Output:- The price 49.10 of Orange

print((f"{3*30}")) #90
print(type(f"{3*30}")) #<class 'str'>

#if i want my string can be shown like :- "hey my name is {} and I am from {}" so we can use like below:-
val1=f"hey my name is {{name}} and I am from {{Country}}"
print(val1) #hey my name is {name} and I am from {Country}