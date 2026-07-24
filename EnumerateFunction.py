# enumerate(): Returns both the index and value while looping through an iterable.
cars=["BMW", "Supra", "OD", "Monalisa", "Mustang"]
for index, cars in enumerate(cars):
    print(index, cars)

'''
OUTPUT:- 
0 BMW
1 Supra
2 OD
3 Monalisa
4 Mustang

If we enter the enumerate(cars, start=1) then output is show from the index 1:-
1 BMW
2 Supra
3 OD
4 Monalisa
5 Mustang
'''


