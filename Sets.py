#SET:- It is a well defined object and unodered collection of data items.It is enclosed with {} brackets
#Sets can't contains duplicate items and its a unchangable, meaning you cannot change items of the set  once created.

s={2,4,2,6}
print(s)
#OUTPUT:-{2, 4, 6}

info={"Harsh",5.9,2,True}
print(info)
#OUTPUT:-{'Harsh', True, 2, 5.9}

#Empty SET:-
emp=set()
print(type(emp))

#OUTPUT:- <class 'set'>

#Accessing the set items:- 
for i in info:
    print(i)

    '''OUTPUT:-
      True
      2
      5.9
      Harsh  
    '''