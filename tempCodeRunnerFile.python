'''
Create a class Book with the following attributes: title, author, and pages.
Write a method get_details() that returns all attributes in a formatted string.
Then, create two objects of this class and call get_details() for both.

'''
class book :
    def __init__(self, title,author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def getdetail(self,):
        return f"book name is {self.title} -{self.author} with {self.pages} pages"
    
b1 = book("shadow slave","guilty3", 2427)
b2 = book("reverened insanity", "gu master", 2334)

print(b1.getdetail())
print(b2.getdetail())



"""
Create a class Student with attributes: name, roll_number, and grade.
Use the __init__ method to initialize these attributes.
Write a method display() to print them in a readable format.
Create one object and call the display method.
"""






'''
Create a class Vehicle with attributes brand and year.
Add a method get_info() that prints the brand and year.
Now create a class Car that inherits from Vehicle and adds a new attribute model.
Override the get_info() method to also include model.
Create a Car object and call get_info().
'''
class vehicle:
    def __init__(self,brand, year):
        self.brand = brand
        self.year = year
    def get_info(self):
        return f"bran of vehicle is {self.brand} and year of manf.. {self.year}"

class car(vehicle):
    def __init__(self,brand , year, model):
        super().__init__(brand , year)
        self.model  = model
    def get_info(self):
        return f"bran of vehicle is {self.brand} and year of manf.. {self.year} having model {self.model}"
    
    
    
car1 = car("maruti", 2024, "swift")


print(car1.get_info())
        





