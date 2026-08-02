#readline() is used to read one line at a time from a file. It returns the next line each time it is called.
f=open("myfile.txt","r")
i=0
while True:
    line=f.readline()
    i=i+1
    if not line:
        # print(line, type(line))
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"Marks of student {i} in Maths is: {m1*2}")
    print(f"Marks of student {i} in English is: {m2*2}")
    print(f"Marks of student {i} in SST is: {m3*2}")
    print(line)

'''
OUTPUT:- Marks of student 1 in Maths is: 12
Marks of student 1 in English is: 34
Marks of student 1 in SST is: 45

12,34,45

Marks of student 2 in Maths is: 67
Marks of student 2 in English is: 54
Marks of student 2 in SST is: 78

67,54,78

Marks of student 3 in Maths is: 45
Marks of student 3 in English is: 67
Marks of student 3 in SST is: 87
45,67,87

    '''


#writelines() is used to write multiple lines (a list of strings) to a file. It does not add a newline (\n) automatically, so you must include \n yourself if needed.

f=open("myfile2.txt","w")
li=["line1\n","line2\n","line3\n"]
f.writelines(li)
f.close()

#Its use where we have a list of strings and we want to write them to a file. It is more efficient than writing each line separately using write() method.
f=open("myfile2.txt","w")
li1=["line1","line2","line3"]
for i in li1:
    f.write(i+ "\n")
f.close()

'''
OUTPUT:- in myfile2.txt file
line1
line2
line3
'''

