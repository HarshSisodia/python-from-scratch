#* map() – Applies a function to every item in an iterable and returns a new iterator with the modified values.
#map(function, iterable)
# def cube(x):
#     return x*x*x

l=[1,2,3,4,5,6,8]
# newl=[]
# for item in l:
#     newl.append(cube(item))
newl=list(map(lambda x: x*x*x, l))
print(newl)

#* filter() – Selects elements from an iterable that satisfy a given condition and returns a new iterator.
#filter(function, iterable)
# def filter_func(a):
#     return a%2==0
newnewl=filter(lambda a: a%2==0,l)
print(list(newnewl))

#* reduce() – Repeatedly applies a function to combine all elements of an iterable into a single value. (Available in the functools module.)
#reduce(function, iterable)
#its also import from functools import reduce
from functools import reduce
# def add(x,y):
#     return x+y
li=[1,2,3,4,5]
Newl=reduce(lambda x,y:x+y,li)
print(Newl)


'''
OUTPUT:-
[1, 8, 27, 64, 125, 216, 512]
[2, 4, 6, 8]
15
'''