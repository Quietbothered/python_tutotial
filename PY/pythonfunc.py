# def my_func():
#     print("muka here")
    
# my_func()
# #giving arg in func
# def my_func(arg1):
#     print(f"{arg1} muka here")
    
# my_func("aambh")
# my_func(my_func('aye'))

# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         merged = []
#         max_len = max(len(word1), len(word2))

#         for i in range(max_len):
#             if i < len(word1):
#                 merged.append(word1[i])
#             if i < len(word2):
#                 merged.append(word2[i])

#         return ''.join(merged)

# solution(word1,word2)
    
def my_function(**kid):
    print(kid)
    for i,j in enumerate(kid):
	    # print(i) 
        print(j)
    # print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

