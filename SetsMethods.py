#Sets Methods:-

#union() Method:-

s1={1,2,3,4,5}
s2={6,7,3,2,8,1}
print(s1.union(s2))

#Update() Method:-
s1.update(s2)
print(s1,s2)

'''OUTPUT:-
{1, 2, 3, 4, 5, 6, 7, 8}
{1, 2, 3, 4, 5, 6, 7, 8} {1, 2, 3, 6, 7, 8}
'''

#Intersection() Method:-

cities={"punjabi bagh","Laxmi Nagar", "Pragati Medan", "NSP"}
cities2={"Rajouri Garden","Laxmi Nagar", "Model Town", "NSP"}
print(cities.intersection(cities2))


#Intersection_Update():-

cities.intersection_update(cities2)
print(cities)

'''
OUTPUT:-
{'Laxmi Nagar', 'NSP'}
{'Laxmi Nagar', 'NSP'}
'''

