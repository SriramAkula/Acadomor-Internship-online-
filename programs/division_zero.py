#Write a program that takes two numbers as input and divides the first number by the second. Use exception handling to manage division by zero.
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    print(numerator/denominator)
except:
    print("Denominator cannot be zero")