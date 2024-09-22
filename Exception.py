#print(10/0)  Zero division error
'''
try:
    num = int(input("Enter the numerator value "))
    deno = int(input("Enter the denominator value "))

    print(num/deno)
except:
    print("Denominator cannot be zero")
    '''
try:
    even_num = [2,4,6,8]
    print(even_num[4])
except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("Denominator cannot be Zero")