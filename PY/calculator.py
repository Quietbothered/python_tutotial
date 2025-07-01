# # Use private variables and a setter/getter method in a class.

# # Create a class with method overloading via default arguments or *args.



# class student :
#     def __init__(self,name , roll):
#         self.__name = name 
#         self.__roll = roll

#     def getname(self):
#         return self.__name
#     def setname(self, new_name):
#         self.__name = new_name
    
    
# s1 = student("ram",101)
# print(s1.getname())
# s1.setname("rohit")
# print(s1.getname())

# class Calculator:
#     def add(self, a=0, b = 0, d = 0):
#         return a + b + d
#     def multiply(self,*args):
#         result = 1
#         for num in args :
#             result *= num
#         return result
# # Write a custom iterator that returns even numbers up to n.

#     def __init__(self , n):
#         self.n = n
#         self.current = 0
        
#     def __iter__(self):
#         return self
        
#     def __next__(self):
#         while self.current<= self.n:
            
#             if self.current % 2 == 0:
#                 even = self.current
#                 self.current += 1
                
#                 return even
#             self.current +=1
#         raise StopIteration


#     # usage
# calc = Calculator()
# even_calc = Calculator(15)
# for num in even_calc:
#     print(num, end  = " ")
# print(calc.add(5))
# print(calc.add(5,10))

# print(calc.multiply(2,3))
# print(calc.multiply(2,4,6))



# '''
# Write a custom iterator that returns even numbers up to n.

# Demonstrate global, local, and nonlocal keyword with small function.

# 🔹 Dates, Math
# Get current date/time and print formatted (dd-mm-yyyy hh:mm:ss).

# Use math module to calculate factorial, square root, and power.

# '''
class person():
    x= 5
    def __init__(self,x):
        self.x = x
        
    
        

abc = person()
print(abc())

class son:
    global x
    x= 5
    def __init__(self,x):
        self.x = x
        return x
    