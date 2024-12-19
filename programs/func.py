'''def display_info(first_name,last_name):
    print("First Name: ",first_name)
    print("Last Name: ",last_name)

display_info(last_name = 'Kumar', first_name='Ravi')
'''
#Arbitary arguments in python
#Program to find sum of multiple numbers
def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result+num

    print("Sum = ",result)

find_sum(1,2,3,4,5)