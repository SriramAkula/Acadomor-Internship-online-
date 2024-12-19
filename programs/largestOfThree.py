num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1 > num2 and num1 > num3:
    print("num1 ",num1," is largest")
elif  num2 > num1 and num2 > num3:
    print("num2 ",num2," is largest")
else:
    print("num3 ",num3," is largest")
