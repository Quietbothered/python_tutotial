x = "global"
def outer():
    x ="outer local"
    
    def inner():
        nonlocal x
        x = "inner modified outer"
        print("inner+",x)
        
    inner()
    print('1outer+', x)
    
outer()
print('Global+', x)


# convert Python dictionary to JSON and back
import json


d1 = {
    "ram": 34
}
jason_str = json.dumps(d1)


b = json.loads(jason_str)
print(b["ram"])


