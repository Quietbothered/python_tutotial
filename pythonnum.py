import random 


#type of variable
x = 1                       #int
y = 35656222554887711.123   #float
z = -3255522j               #complex number

print(type(x))
print(type(y))
print(type(z))

#float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#float using e(all with power e4=10^4 are in float data type)
x = 35e3
y = 12E4
z = -87.7e100
print (x,y,z)
print(type(x))
print(type(y))
print(type(z))
#convert int to float and complex and float to int
x = 1                       #int
y = 711.123   #float
z = -3255522j               #complex number

a=float(x)
b=int(y)
c=complex(x)
print (a,b,c)
print(type(x))
print(type(y))
print(type(z))

print(random.randrange(10,100))
s=int("11214")
print(s,type(s))
