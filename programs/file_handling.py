#one way
# file = open("data.txt",'r')

# for each in file:
#     print(each)
   
     
#2nd way
#print(file.read())

#3rd way
 
'''
with open("data.txt") as file:
    data = file.read()

print(data)'''

# file = open("data.txt",'w')
# file = open("data.txt",'a')
# file.write("This is new content appended to the file")
# file.close()

with open("file.txt",'w') as f:
    f.write("Hello World")