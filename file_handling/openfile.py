# # f = open("theory.md")
# # f = open(r"C:\Users\91878\python_tutotial\file_handling\theory.md", "r")
# with open(r"C:\Users\91878\python_tutotial\file_handling\theory.md", "r") as f:



#     # print(f.read())
    
#     # print(f.readline) #gives just what is objet not calls 
#     # f.close()
#     for x in f:
#         print(x)
    
#     f.close()

# with open(r"C:\Users\91878\python_tutotial\file_handling\theory.md", "a") as f:
#     f.write("\n hola im writing to append in file")

# with open(r"C:\Users\91878\python_tutotial\file_handling\theory.md", "r") as f:
#     print(f.read())

# with open(r"C:\Users\91878\python_tutotial\file_handling\theory.md", "w") as f:
#     f.write("ohhh nooo i deleted it whole")
    
# with open(r"C:\Users\91878\python_tutotial\file_handling\theory.md", "r") as f:
#     print(f.read())

import os


if os.path.exists(r"C:\Users\91878\python_tutotial\file_handling\theory.md"):
    os.remove(r"C:\Users\91878\python_tutotial\file_handling\theory.md")
    print("file deleted")
else :
    print("it does not exist")



# os.rmdir("foldername\\path") # only deletes empty folders