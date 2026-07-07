#Tuple:- not changeable
tup=(1,3,5)
print(type(tup), tup)

tup1=(1)
print(type(tup1), tup1) #Its print integer type because python don't know we want to make integer value.
#So if we want to make a single value is a tuple so we use comma like example:- tup1=(1,)

tup2=(1,4,5,"Harry",4.5)
print(tup2)
print(tup2[0])
print(tup2[1])
print(tup2[2])
print(tup2[3])
print(tup2[-1])
print(tup2[-2])


if 4 in tup2:
    print("Yes")

else:
    print("No")


if "ry" in "Harry":
    print("yes")
else:
    print("No")


#Slicing:-
print(tup2[0:5:1])
tup3=tup2[0:5:1]
print(tup3)
print(tup2[1:3])


'''Output:-
<class 'tuple'> (1, 3, 5)
<class 'int'> 1
(1, 4, 5, 'Harry', 4.5)
1
4
5
Harry
4.5
Harry
Yes
yes
(1, 4, 5, 'Harry', 4.5)
(1, 4, 5, 'Harry', 4.5)
(4, 5)
'''