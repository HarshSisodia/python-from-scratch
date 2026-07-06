#List:- It is a collection of items that are ordered and changeable. It allows duplicate members.
myList=["apple", "banana", "cherry"]
print(myList)
print(type(myList)) #it will print the type of the variable myList which is list.
print(myList[0]) #it will print the first item of the list.
print(myList[1]) #it will print the second item of the list.
print(myList[2]) #it will print the third item of the list.


myList2=[1,"Harry", "Potter", 4.5, True] #List can contain different data types.
print(myList2)
print(myList2[0]) #it will print the first item of the list.
print(myList2[1]) #it will print the second item of the list.
print(myList2[2]) #it will print the third item of the list.

#Negitive Indexing:- It is used to access the items of the list from the end of the list.
print(myList2[-1]) #it will print the last item of the list.
print(myList2[-2]) #it will print the second last item of the list.
print(myList2[len(myList2)-3]) #it will print the third last item of the list.


#Check wheather an item is present in the list.

color= ["red", "green", "blue", "yellow", "orange"]
if "blue" in color:
    print("Yes, 'blue' is present in the list.")    
else:
    print("No, 'blue' is not present in the list.")

#Same thing applies for the string as well.
# if "reen" in "green":
#     print("Yes")

#Start to end indexing:- It is used to access the items of the list from the start to end of the list.
print(color[:])
print(color[1:])
print(color[1:-1])

#Jumping indexing:- It is used to access the items of the list with a specific step size.
print(color[0:4:2]) #it will print the first and third item of the list.
print(color[-1:-5:-1]) #it will print the last item to the first item of the list in reverse order.
print(color[len(color)-1:len(color)-5:-1]) #it will print the last item to the first item of the list in reverse order and above print is same.


#LIST COMPREHENSION:- It is a concise way to create lists.
lst=[i for i in range(5)] #it will create a list of numbers from 0 to 5
print(lst)
lst2=[i for i in range(10) if i%2==0] #it will create a list of even numbers from 0 to 10
print(lst2)

names=["Harry", "Potter", "Ron", "Weasley"]
name2=[i for i in names if "a" in i] #it will create a list of names which contains the letter "a"
print(name2)



