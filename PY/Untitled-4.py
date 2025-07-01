'''

Create a class Student with name, roll number; print details using a method.

Add a constructor (__init__) to initialize attributes.

Create a class Vehicle and inherit it into Car; add method to display both details.

Override a method from the parent in child class.
'''

class student :
    def __init__(self,name , roll_no):
        self.name = name
        self.roll_no = roll_no
        
    def detail (self,):
        print(f"his name is {self.name}  and roll is {self.roll_no}")
        
        
a = student("rahul",26)
a.detail()




