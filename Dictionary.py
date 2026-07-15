#Dictionary:- dictionary are ordered collection of data item.They store multiple items in single variable.
#Dictionary items are key-value pair that are seperate by commas and enclosed within curly brackets{}.

dict={
    567:"Harry",
    765:"Shubham",
    543:"Raj",
    987:"Honey"
}

print(dict[567])
print(dict.get(567))

print(dict)
print(dict.keys())
print(dict.values())

for key in dict.keys():
    print(f"The value corresponding to the key {key} is {dict[key]}")


print(dict.items())
for key,value in dict.items():
    print(f"The value corresponding to the key {key} is {value}")


'''OUTPUT:- 
Harry
Harry
{567: 'Harry', 765: 'Shubham', 543: 'Raj', 987: 'Honey'}
dict_keys([567, 765, 543, 987])
Harry
Shubham
Raj
Honey

Harry
Shubham
Raj
Honey

The value corresponding to the key 567 is Harry
The value corresponding to the key 765 is Shubham
The value corresponding to the key 543 is Raj
The value corresponding to the key 987 is Honey


dict_items([(567, 'Harry'), (765, 'Shubham'), (543, 'Raj'), (987, 'Honey')])
The value corresponding to the key 567 is Harry
The value corresponding to the key 765 is Shubham
The value corresponding to the key 543 is Raj
The value corresponding to the key 987 is Honey

'''
