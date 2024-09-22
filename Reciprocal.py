'''num = int(input("Enter a number: "))
if num%2 == 0:
    try:
        print("Reciprocal of the number is 1 /",num)
    except:
        print("Zero division error")'''
try:
    num = int(input("Enter the number: "))
    assert num%2 == 0
except:
    print("Not an ven number")
else:
    reciprocal = 1/num
    print(reciprocal)
finally:
    print("This is finally block")