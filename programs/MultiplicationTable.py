#Write a program that prints the multiplication table for a given number n using a while loop.
def multiplication_table(num):
    i=1
    while i<=10:
        print(num,"x",i,"=",num*i)
        i=i+1



num = int(input("Enter the number: "))
print("Multiplication table of",num,"is")
multiplication_table(num)