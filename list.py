# normal for loop
'''num = [1,2,3,4,5]
new_list = []

for i in num:
    new_list.append(i*i)

print(new_list)

#single line for loop
num = [1,2,3,4,5]
new_list = [i*i for i in num]

'''
even_num = [num for num in range(1,10) if num%2==0]
print(even_num)