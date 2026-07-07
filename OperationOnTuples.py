color=("Red","Yellow","blue","Orange","Black","White")
temp=list(color)
#Add:-
temp.append("pink")
print(temp)

#Remove:-
temp.pop(1)
print(temp)

#Change:-
temp[1]="Green"
print(temp)

color=tuple(temp)
print(color)

#Concatenate:-
Number=(1,2,31,4,5,6,1,2,3,54,321,3214,6,5,32,2,1,35,31,2,8)
print(len(Number))
concat=color+Number
print(concat)


# TupleMethods:-

#Count() Method:-
print("Count of 1 n tuple: " , Number.count(1))

#Index() Method:-

print("First Occurance 3 is: ", Number.index(3))

print("Range Occurance index of 1 is: ", Number.index(1,8,21))
