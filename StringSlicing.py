name="Harry, shubham, rohit"
print(name[0:3]) #Harry
print(name[7:10]) #shubham
print(name[12:15]) #rohit

'''
OUTPUT:
Har
shu
am,
'''

fruits="Mangoes, Bananas, Grapes, Oranges"
print(len(fruits)) #length of the string
print(fruits[5]) # it will print the 5th character of the string
print(fruits[:9]) #it will print the first 9 characters of the string
print(fruits[:]) #it will print the whole string
print(fruits[0:-3]) #it will print the whole string except the last 3 characters
print(fruits[0:len(fruits)-3]) #it will print the whole string except the last 3 characters and above print is same.
print(fruits[0:len(fruits)-3:2]) #it will print the whole string except the last 3 characters and it will print every second character of the string.

print(fruits[-1:-3]) #it will print nothing because the starting index is greater than the ending index.
print(fruits[-3:-1]) #it will print the last 2 characters of the string.




'''output: In this commas and spaces are also counted in the length of the string.
and len() can be used to find the length of any string.
33
e
Mangoes, 
Mangoes, Bananas, Grapes, Oranges
Mangoes, Bananas, Grapes, Oran
Mangoes, Bananas, Grapes, Oran
Mnos aaa,Gae,Oa

ge
'''


#QUICK QUIZ:-

nm="Harry Potter"
print(len(nm))
print(nm[-4:-2]) #Solution is "tt"


