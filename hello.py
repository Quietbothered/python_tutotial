'''
Python Syntax
Python Comments
Python Variables
Python Data types
'''


if 5>2 :
    
    print('true')
x= 4
#x= int(input("enter no\n"))
x="hello"
print(x)
#x= 5.003
print(type(x)) # return datatype of variable

#basic variable 

#set multiple variables with same value
x = y = z = "Orange"
print(x)
print(y)
print(z)
# printing variabeles with 
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#addition of string 
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#function 

#define function and using variable outside the function 
x = "awesome"

def myfunc():
    print("Python " + x)

myfunc()

#output of function

x = "awesome"
def myfunc1() :
    print("ok")
    
myfunc1()


#local and global variable in a function 
x = "awesome"

def myfunc2():
    x = "fantastic2"
    print("Python is " + x)

myfunc2() #return with fantastic2

print("Python is " + x) #returns with awsome

#defining global function
#both prints will use x= one

def myfunc3():
    global x
    x = "one"
    print ("python is ", x)
myfunc3()
print ("python is ", x)

#frozen set

y = frozenset({"apple", "banana", "cherry"})
print(y)
y = frozenset(["apple", "banana", "cherry"])

print(y)


#bytes
x= b"abc"
print(x)
print(type(x))



