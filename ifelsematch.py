'''
x,y=35,20                   #shorthand ifelse
print("x larger") if x>y else print("y larger")'''
print('hola')
a = 200
b = 33
c = 500
if a > b or a > c :
    print("At least one of the conditions is True")

if (a > b) | (a  > c) :
    print("bit wise or At least one of the conditions is True")

def check_left():
    print("Left checked")
    return True

def check_right():
    print("Right checked")
    return False
if check_left() or check_right():
    print("Done")
elif check_left() & check_right():
    print("Done1")

elif check_left() | check_right():
    print("Done2")
#guarded match cases
a =85
match a:
    case _ if a>=90:
        print('c1')
    case _ if a>70:
        print('c3')
    case _ if a>80:
        print('c2')
        

#while loop
x=9
i=0
while i < x:
    print(i,end=" ")
    if i==3:
        print("00000000")
        break
    
    i+=1
i=0
print('')
while i < x:
    i+=1
    print(i,end=" ")
    if i==3:
        print("00000")
        continue    
    
while True:
    pass

while True:
    command = input("type alpha")
    if command== 'alpha':
        break
print('you typed', command)












