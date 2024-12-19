# Write a function named calculate_factorial that takes a single integer argument n and returns the factorial of n.
def calculate_factorial(num):
    res = 1
    for i in range(1,num+1):
        res*=i
    return res



num = int(input("Enter number: "))
res = calculate_factorial(num)
print("Factorial of",num,"is", res)