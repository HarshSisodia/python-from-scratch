# By Enter a name and print each character of the name using for loop
name= input("Enter your name: ") 
for i in name:
    print(i, end=", ") 

''' Output: 
Enter your name: Tushal
T, u, s, h, a, l, % '''


# By List 
Animal=["Dog", "Cat", "Cow", "Horse", "Lion", "Tiger"] 
for j in Animal:
    print(j, end=", ")
    for k in j:
        print(k, end=", ")

''' Output: Dog, Cat, Cow, Horse, Lion, Tiger 
Dog, D, o, g, Cat, C, a, t, Cow, C, o, w, Horse, H, o, r, s, e, Lion, L, i, o, n, Tiger, T, i, g, e, r, % '''


# Range function
for l in range (10):
    print(l+1)

    '''
    Output:
    1
    2
    3
    4
    5   
    6
    7
    8
    9
    10
    '''

for l in range (10, 20):
    print(l+1)

''' Output:
10
11
12
13
14
15
16
17
18
19
20
'''

for l in range (0, 50, 5): #5 is a step value which is used to increment the value of l by 5
    print(l)

''' Output:
0
5
10
15
20
25
30
35
40
45
'''

