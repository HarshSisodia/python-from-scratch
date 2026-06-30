#String are immutable
a="Harsh"
print(len(a))
print(a.upper())
print(a.lower())

'''OUTPUT:
5
HARSH
harsh
'''


#rstrip() removes all the whitespace characters from the right end of the string
b="!!!!Harry!!!!!!!!"
print(b.rstrip("!"))

'''OUTPUT: !!!!Harry'''


#Replace() method replaces a specified phrase with another specified phrase and all occurrences of the specified phrase will be replaced.
c="I like Java. Java is a programming language."
print(c.replace("Java","Python"))

'''OUTPUT: I like Python .Python is a programming language.'''


#split() method splits the string into a list.
d="I like python programming"
print(d.split(" "))

'''OUTPUT: ['I', 'like', 'python', 'programming']'''


#capitalize() method returns a string where the first character is upper case, and the rest of the characters are lower case.
e="python is a programming language"
f="python iS A PROGRAMMING LANGUAGE"
print(e.capitalize())
print(f.capitalize())

'''OUTPUT: Python is a programming language
Python Is A Programming Language'''

#center() method returns a centered string of a specified length.
g="Welcome to the Python programming"
print(g.capitalize())
print(len(g))
print(len(g.center(50)))
print(g.center(50))

'''OUTPUT: Welcome to the python programming
33
50
         Welcome to the Python programming          '''

#count() method returns the number of times a specified value occurs in a string.
h="I like python programming. python is a programming language."
print(h.count("p"))
print(h.count("python"))

'''OUTPUT: 4
2'''


#endwith() method returns True if the string ends with the specified value, otherwise False.
i="I like python programming !!"
print(i.endswith("!!"))

i="I like python programming !!"
print(i.endswith("yt", 4, 10))

'''OUTPUT: True
True'''


#find() method returns the lowest index of the substring if it is found in a given string. If it is not found then it returns -1.
j="I like python programming. python is a programming language."
print(len(j))
print(j.find("a")) # its find first occurrence of a
print(j.find("aww")) #returns -1 because aww is not present in the string

'''OUTPUT: 60
19
-1'''

#isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers) and there is at least one character, otherwise it returns False.
k="Python3"
l="Python"
m="Python 3"
print(k.isalnum())
print(l.isalnum())
print(m.isalnum())

'''OUTPUT: True
True
False'''



#isalpha() method returns True if all characters in the string are alphabets and there is at least one character, otherwise it returns False.
n="Welcome"
o="Welcome1234"
p="Welcome 1234"
print(n.isalpha())
print(o.isalpha())
print(p.isalpha())

'''OUTPUT: True
False
False'''


#islower() method returns True if all characters in the string are lower case and there is at least one character, otherwise it returns False.
q="welcome harry"
r="WelcomeHarry"
print(q.islower())
print(r.islower())

'''OUTPUT: True
False'''


#isupper() method returns True if all characters in the string are upper case and there is at least one character, otherwise it returns False.
s="WELCOME HARRY"
t="WelcomeHarry"
print(s.isupper())
print(t.isupper())  

'''OUTPUT: True 
False'''

#isprintable() method returns True if the string is printable, otherwise it returns false. such as escape character \n.
s="Hello\nWorld"
t="Hello World"
print(s.isprintable())
print(t.isprintable())

'''OUTPUT: False
True'''


#isspace() method returns True if all characters in the string are whitespaces, otherwise it returns False.
u="Harry Potter"
v="   " #Using SPACE
w="    "  #using TAB 
print(u.isspace())
print(v.isspace())
print(w.isspace())

'''OUTPUT: False
True
True'''


#istitle() method returns True if the string follows the rules of a title, otherwise it returns False.
x="Harry Potter"
y="To kill a mockingbird"
print(x.istitle())
print(y.istitle())

'''OUTPUT: True
False'''


#startswith() method returns True if the string starts with the specified value, otherwise it returns False.
z="I like python programming"
a="I like python programming"
print(z.startswith("I like"))
print(a.startswith("man"))
print(a.startswith("like", 2, 10))

'''OUTPUT: True
False
True'''


#swapcase() method returns a string where all the upper case letters are lower case and vice versa.
b="i like python programming"
c="I LIKE PYTHON PROGRAMMING"
print(b.swapcase())
print(c.swapcase())


'''OUTPUT: I LIKE PYTHON PROGRAMMING
i like python programming'''



#title() method returns a string where the first character in every word is upper case and all other characters are lower case.
d="i like python programming"
e="I LIKE PYTHON PROGRAMMING"
print(d.title())
print(e.title())

'''OUTPUT: I Like Python Programming
I Like Python Programming'''
