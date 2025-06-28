#-------------operator------------
# = - * / add sub mul divide
# % modulus(remainder is returned)
# ** exponential a**b a to the power b
# // floor division removes decimal part after division/ quotient
# a+=1 --> a=a+1, simarly a-=1,a*=4,a/=3,a%=2,a**=3
'''
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)
'''
#&=	x &= 3	x = x & 3	
x=6
x&=3
print(x)#returns and operation of x&3

#|=	x |= 3	x = x | 3	
x=5
x|=3
print(x)

#^=	x ^= 3	x = x ^ 3
x=7
x^=3    #it is xor operation exclusive or
print(x) 

#>>=	x >>= 3	x = x >> 3	
x>>=3 #shifts binary value right by 3 positions /divide by 2^3
#same for right shift operator

print(x:=3) #helps us assign on spot





#--------------list----------------
l1=["abc",'qwerty','apple']
print(l1)
print(type(l1))
l2=list(("alpha",'qwer','ape'))
print(l2)

l1.append('raone')      #append
print(l1)
l1.insert(1,'arvind')   #insert at a  location 
print(l1)
l1.extend(l2)           #extend to another list
print(l1)
l1.pop(1)
print(l1)               #pop operator
l1.remove('apple')
print(l1)
del l1[0]            #del removes with specific keyword removes whole list if index not specified
print(l1)  
del l1  #  there are no l2 list further 
print(l2)  
l2.clear()
print(l2)

l1=["abc",'qwerty','apple']
for i in range(len(l1)):
    print(l1[i])

i=0
while i<len(l1):
    print(l1[i])
    i+=1
    
#returning specific string with "a" in it
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
l3=[]

for i in fruits:
    if "a" in i:
        l3.append(i)
    
print(l3)

#with list comprension
l3 =[i for i in fruits if i!="apple" ]
print(l3)

newlist = [x if x != "banana" else "orange" for x in fruits]

# sorting with key = a funcion
def myfunc(n):
    return abs(n-50)
l4=[34,56,78,100,25,47]
l4.sort(key = myfunc, reverse=True)
print(l4)

#copying a list to new list
l5=l4.copy()
print(l5)
l6=list(l3)
print(l6)

mylist=l6[:]
print(mylist)

#joining 2 list
l7=l3+l5
print(l7)
#print(l7.sort())
l7.append(l1)
print(l7)
l7.clear()

#append a new list in another
for x in l3:
    l7.append(x)
#joining 2 list 
print(l7)
l7.extend(l1)
print(l7)



