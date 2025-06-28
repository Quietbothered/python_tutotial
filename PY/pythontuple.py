t1 =("abc", 34, True, 40, "male")
print([i for i in t1])
t2 = tuple(("apple", "banana", "cherry"))
a1 =["abc", 34, True, 40, "male"]
#t3=a1.join(t1)
print()

print(t1[1])
#append in tuple using list
l1=list(t1)
l1.append('kiwi')
l1[1]=365
l1.insert(3,'ravindra')
t1=tuple(l1)
print(t1)
#unpacking tuple
(qwe,*red)=t1
print(qwe)
print(red)
#accesing elen=ments in tupple
for i in range(len(t1)-1,0,-1):
    print(t1[i])
#multipluing tupple
print(t2*2)


#set------------

thisset = {"abc", 34, True, 40, "male"}
print(thisset)
s1=set(("apple", "banana", "cherry"))
print(s1)

l1=list([["abufbe",],['uwefu','jewnfj']])
thisset.add('ory')
#thisset.update(s1)          #iterable can be anything list tuple dict
print(l1)
print(thisset)
s1=s1.union(thisset)
print(s1)


l2 = [[]]
l2.append(['1ws','1s1','qds'])
print(l2)
#update - s1.update(value/set), union, intersection, difference, symmetric_difference



t1 =["abc","male"]

b='asnuiabfbdj'
c=' '.join(t1)
print(c)
#dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])





#dictionaries
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})

#nested dictionary

child1 = {
    "name" : "Emil",
    "year" : 2004
    }
child2 = {
    "name" : "Tobias",
    "year" : 2007
    }
child3 = {
    "name" : "Linus",
    "year" : 2011
    }

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
    }


#nested for loop to return item and values of dictionary
for x,obj in myfamily.items():
    print(x)
    for y in obj :
        print(y,obj[y])





