marks1 = int(input("Enter marks of subject1: "))
marks2 = int(input("Enter marks of subject2: "))
marks3 = int(input("Enter marks of subject3: "))

avg_marks = (marks1+marks2+marks3)/3
print("Average marks is: ",avg_marks)

if avg_marks>=90:
    print("Grade A")
elif avg_marks>=80 and avg_marks<90:
    print("Grade B")
elif avg_marks>=60 and avg_marks<80:
    print("Grade c")
else:
    print("Grade D")