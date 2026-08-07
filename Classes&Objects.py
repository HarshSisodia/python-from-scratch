class Person:
    name="Bamae"
    age=20
    occupation="Student"
    course="Python Programming"
    # self paramter mean the instance of the class. It is used to access variables that belongs to the class.
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a=Person() # This is a way to creat an object of a class
b=Person() # This is a way to creat an object of a class
a.name="luv"
a.age=21
a.occupation="Engineer"

b.name="Ravi"
b.occupation="Doctor"
#print(a.name,a.age,a.occupation,a.course)
a.info()
b.info()