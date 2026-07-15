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

#Symmetric_difference():-

citi={"punjabi bagh","Laxmi Nagar", "Pragati Medan", "NSP"}
citi2={"Rajouri Garden","Laxmi Nagar", "Model Town", "NSP","moti Nagar"}
print(citi.symmetric_difference(citi2))
citi.symmetric_difference_update(citi2)
print(citi)

#OUTPUT:- {'punjabi bagh', 'Model Town', 'Rajouri Garden', 'Pragati Medan'}



#difference() & difference_update():-

cit={"punjabi bagh","Laxmi Nagar", "Pragati Medan", "NSP"}
cit2={"Rajouri Garden","Laxmi Nagar", "Model Town", "NSP"}
print(cit.difference(cit2))

#OUTPUT:- {'punjabi bagh', 'Pragati Medan'}


#isdisjoint():- method to check if item of given set are present in another set.
a={"punjabi bagh","Laxmi Nagar", "Pragati Medan", "NSP"}
a1={"Rajouri Garden","Laxmi Nagar", "Model Town", "NSP"}
print(a.isdisjoint(a1))

#OUTPUT:- False

#issuperset():- Method to check if all item of a particular set are present in the original set.
a={"punjabi bagh","Laxmi Nagar", "Pragati Medan", "NSP"}
a1={"Rajouri Garden", "Model Town"}
print(a.issuperset(a1))

#OUTPUT:- False


#issubset():- method to check if all the items of the original set are present in the particular set.
a={"punjabi bagh","Laxmi Nagar", "Pragati Medan", "NSP"}
a1={"Laxmi Nagar","NSP"}
print(a1.issubset(a))

#OUTPUT:- True


# add():-
b={"punjabi bagh","Laxmi Nagar", "Pragati Medan", "NSP"}
b.add("Kirti Nagar")
print(b)

#OUTPUT:-{'NSP', 'Kirti Nagar', 'Pragati Medan', 'punjabi bagh', 'Laxmi Nagar'}

#Update():-
b={"punjabi bagh","Laxmi Nagar", "Pragati Medan", "NSP"}
b1={"preet vihar","NSP"}
b.update(b1)
print(b)

#OUTPUT:- {'preet vihar', 'Laxmi Nagar', 'NSP', 'Pragati Medan', 'punjabi bagh'}


#REMOVE()/DISCARD():- if we use dicard the it can't throw the error but remove through error bcz if that material we want to remove is not same so it show error

b={"punjabi bagh","Laxmi Nagar", "Pragati Medan", "NSP"}
b.remove("NSP")
print(b)

#OUTPUT:-{'punjabi bagh', 'Pragati Medan', 'Laxmi Nagar'}


#POP():- It remove any item from a set and we can access that value which is remove 
b={"punjabi bagh","Laxmi Nagar", "Pragati Medan", "NSP"}
c=b.pop()
print(b)
print(c)
#OUTPUT:- {'punjabi bagh', 'Laxmi Nagar', 'NSP'}
#Laxmi Nagar



#del():- its helping to delete whole set
ci={"punjabi bagh","Laxmi Nagar", "Pragati Medan", "NSP"}
del ci
# print(ci)

#OUTPUT:-it show NameError because we delete the set.

#Clear():- which helping to clear the set items and show the empty set.

d={"punjabi bagh","Laxmi Nagar", "Pragati Medan", "NSP"}
d.clear()
print(d)

#OUTPUT:- set()



#check if item is present or not:-

info={"Harsh",5.9,2,True}

if 5.9 in info:
    print("Yes")    
else:
    print("NO")

    #OUTPUT:- Yes
