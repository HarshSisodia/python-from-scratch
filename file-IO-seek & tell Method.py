#seek() is used to move the file pointer to a specific position in a file.
#tell() is used to return the current position of the file pointer in a file.
with open("file.txt","r") as f:
    # print(type(f))
    f.seek(10) #seek() method is used to move the file pointer to a specific position in the file. The argument passed to seek() is the number of bytes to move from the beginning of the file.

    print(f.tell()) #tell() method is used to get the current position of the file pointer. It returns the number of bytes from the beginning of the file.

    data=f.read(5) #read() method is used to read a specific number of bytes from the file. The argument passed to read() is the number of bytes to read.
    print(data)




#truncate() is used to resize a file to a specified number of bytes. It removes any data beyond that size.
with open("sample.txt","w") as g:
    g.write("Hello World")
    g.truncate(5) #truncate() method is used to resize the file to a specified number of bytes. The argument passed to truncate() is the number of bytes to keep in the file. Any data beyond that size will be removed.
    with open("sample.txt","r") as g:
        print(g.read()) #Output: Hello



'''
OUTPUT:-
10
ethar
Hello
'''