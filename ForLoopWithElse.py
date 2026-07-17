# In Python, we can use an else block with a for loop; it executes when the loop completes normally without a break.
for i in range(5):
    print(i)
else:
    print("Sorry No i")

'''
OUTPUT:- 
0
1
2
3
4
Sorry No i
'''

#Example 2:-

for i in range (5):
    print("iteration no {} in for loop".format(i))
else:
    print("else block in loop")
print("Out of the loop")


'''
OUTPUT:-
iteration no 1 in for loop
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
else block in loop
Out of the loop
'''


#Loop break and no else should be print 
for j in range(6):
    print(j)
    if j==4:
     break
else:
    print("sorry no j")

'''
OUTPUT:- 
0
1
2
3
4
'''