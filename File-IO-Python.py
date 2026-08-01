#Opening a file in Python means creating a connection between your program and the file so you can read, write, or modify its contents.

'''    
* Read (r) → Reads the content of an existing file without changing it.
* Write (w) → Writes data to a file and overwrites its existing content.
* Append (a) → Adds new data to the end of a file without deleting existing content.
* Create (x) → Creates a new file and gives an error if the file already exists.
* Binary (b) → Opens a file in binary mode to read or write non-text data (e.g., images, videos, PDFs).
'''

#Reading :-
f=open("myfile.txt","r") #open file in read mode
# print(f)
txt=f.read()
print(txt)
f.close() #closing the file after reading

#write:-
g=open("myfile.txt","a") 
# print(g)
txt1=g.write("Hello, World!")
print(txt1)
g.close()


#with:- The with statement opens a file and automatically closes it after the block of code is executed.

with open("myfile.txt","a") as f:
    f.write("The world is beautiful")
