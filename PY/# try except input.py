

# try except input

y=True
while y==True:
    x=input('enter integer')
    try:
        x=float(x)
        y=False
    except:
        print('try again')
    
print('thankyou')








{
     "name": "John",
     "age": 30,
     "married": true,
     "divorced": false,
     "children": [
          "Ann",
          "Billy"
     ],
     "pets": null,
     "cars": [
          {
               "model": "BMW 230",
               "mpg": 27.5
          },
          {
               "model": "Ford Edge",
               "mpg": 24.1
          }
     ]
}