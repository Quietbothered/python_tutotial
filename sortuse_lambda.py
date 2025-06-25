'''data = [(1, 3), (2, 2), (3, 1)]
# Expected output: [(3, 1), (2, 2), (1, 3)]
'''

data = [(1, 3), (2, 2), (3, 1)]
# Expected output: [(3, 1), (2, 2), (1, 3)]

c = sorted(data,key = lambda x:x[1])
data.sort(key = lambda x:x[1])
y = lambda data:data[1]
print(y[2])

print(data)