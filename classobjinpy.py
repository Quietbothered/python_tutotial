'''
oop concepts

'''
class myclass():
    x=5

alp = myclass()
class aero:
    y=6
print(f'{aero} is aero class')

# alp2 = myclass()
# alp1 = myclass()
# alp0 = myclass()
print(myclass())
print(alp.x)


class person:
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def __str__(self):
        return f"{self.name} ({self.age})"
    # return name 
p1 = person('jonny',39)
print(p1)
print(p1.age,p1.name,)

#use or other name in place of self
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("Johncena", 36)
p1.myfunc()





