name="Harsh"
Friend="Rohit"
anotherFriend="Sahil"
mango='He said, "I want to eat mangoes."' #or we can use "\\"

print("Hello " + name)
# print("Hello " + Friend)
# print("Hello " + anotherFriend)
# print(mango)


#Multiline String
multilineString = """This is a multiline string.
It can span multiple lines.
You can use triple quotes to create it."""  

# print(multilineString)


print(name[0]) #H
print(name[1]) #a
print(name[2]) #r
print(name[3]) #s
print(name[4]) #h   
# print(name[5]) #IndexError: string index out of range
print("Lets use a for loop\n")
# for using for loop:-

for i in multilineString:
    print(i) #it will print each character in the string