'''greet = lambda name: print("Hello ",name)
greet("Rohan")'''

#program to filter even items

list1 = [1,5,4,6,8,9,11,23,12]
# list2 = list(filter(lambda x:(x%2==0),list1))
# print(list2)

list2 = list(map(lambda x:x*2,list1))
print(list2)