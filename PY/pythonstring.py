print('hieee')
print("hola")
print('hieee"hola"')
a= '''this is string 
in three 
lines hola'''
print(a)

#printing each character of string banana
for x in "banana":
    print(x,end ="")
    
#length of string
print ('\n',len(a))  #\n for new line ,(coma )adds space before 3
print ('\n',len(a))  #without space before outout
print('\n', len(a), sep='')
print('\n' + str(len(a)))

#a sub strung present in another string
txt = "ram is a good boy"

if "ram" in txt :
    print( '   ram is present in string   ')

#slicing string
print ( txt[:5])

print ( txt[7:])
#reverse index use
print ( txt[-2:])
#printing reverse string
print ( txt[::-1])
#all upper case
print ( txt.upper())
#all lower case
print ( txt.lower())
#removing whitespace from beginning and end
print ( txt.strip())
#replacing char of string
a = "Hello, World!"
print(a.replace("H", "J"))
#splitting at designated character that particular character is ommited from both strings
print(a.split("o"))

## concatenation of string(joining 2 strings)
c=txt +a
print(c)

c=txt+' ab'+a
print(c)
#formating string
age =21
te = f'there are 26 letters, age {age}'

print(te)

te = f'there are 26 letters, age {age:.2f}' #display placeholder/number with 2decimal points
print(te)
te = f'there are 26 letters, age {56*65}'
print(te)
#encode a part of string i.e before \r
tf = f'there are 26 \rletters, age {age}'
print(tf)

#find()uses
if te.find('re')!=-1:
    print('found!.....')
    
#___________________bool_____________

print(10 > 9)
print(10 == 9)
print(10 < 9)
print(bool('hello'))
print(bool(35<33))
print(bool(None))
print(f"alpha{te}",bool({}))

print(f"alpha{tf}",bool({}))
#myclass return 0 as value which bool function gives false as result
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#use function as bool
def myFunction() :
    return True

print(myFunction())

# check if object is int or not
x = 200
print(isinstance(x, int))
x = 'rohan'
print(isinstance(x, str)) #simmilar implementation for other data types


