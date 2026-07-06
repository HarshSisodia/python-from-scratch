#list.sort() method is used to sort the list in ascending order by default. It can also take a parameter reverse=True to sort the list in descending order.
myList3=[11, 34, 3, 1, 4, 2, 5,5]
myList3.sort() #it will sort the list in ascending order.
print(myList3)
# myList3.sort(reverse=True) #it will sort the list in descending order.
# print(myList3)

#Reverse() method is used to reverse the list. It does not take any parameters.
myList3.reverse() #it will reverse the list.
print(myList3)

#append() method is used to add an item to the end of the list.
myList3.append(6) #it will add 6 to the end of the list
print(myList3)



#index() method is used to find the index of an item in the list. It takes one parameter which is the item to be searched.
print(myList3.index(4)) #it will print the index of 4 in the list which is 3.


#Count() method is used to count the number of occurrences of an item in the list. It takes one parameter which is the item to be counted.
print(myList3.count(5)) #it will print the number of occurrences of 5


#Copy() method is used to create a copy of the list. It does not take any parameters.
# Don't use until you are begineer.
# myList4=myList3 #it will create a copy of myList3 and store it in myList4
# myList4[0]=0
# print(myList3) #Output:-[0, 11, 5, 5, 4, 3, 2, 1, 6]

#so use copy method 
myList4=myList3.copy()
myList4[0]=0
print(myList3) #Output:- [34, 11, 5, 5, 4, 3, 2, 1, 6]


#insert() method :- It is used for intersting the value of any index which we want to change the existing value
myList3.insert(0,"start")
print(myList3)


#extend() method :- new list can be adding in old list if we want 

m=[800,900,1000]
myList3.extend(m)
print(myList3) #Output:- ['start', 34, 11, 5, 5, 4, 3, 2, 1, 6, 800, 900, 1000]



#concatenate of two list:-

new=[500,600,700]
k=myList3+new
print(k)  #Output:- ['start', 34, 11, 5, 5, 4, 3, 2, 1, 6, 800, 900, 1000, 500, 600, 700]






