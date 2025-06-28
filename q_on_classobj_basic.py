'''**Easy:**
1.  What is the fundamental difference between a "class" and an "object" in Python?
2.  How do you define a minimal, empty class named `Car`?
3.  Write the line of code to create an instance (or object) of a class named `Car`.
'''
class car:
    pass

a = car()
print(a)

'''
**Medium:**
4.  Explain the difference between a class variable and an instance variable with a simple example.
5.  What is the purpose of the `self` parameter in a class method, and why is it necessary?
 '''
class student :
    def __init__(self, name):
        self.name = name 
    def greet(self):
        
        print(f"hello my name is {self.name}")
        return "alpha"
    
s1 = student('rahul')
s1.greet()
print(s1.greet(),)

'''**Tough:**
6.  Discuss the concept of "monkey-patching" in Python. How could you add a new method to an existing class at runtime, and what are the potential risks of doing so?
'''










