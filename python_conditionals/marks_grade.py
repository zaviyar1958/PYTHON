marks = float(input("Enter your marks: "))
if (marks > 90 and marks <= 100):
    print("Grade A")
elif(marks > 75 and marks <= 90):
    print("Grade B")
elif(marks > 50 and marks <= 75):
    print("Grade C")
elif(marks >= 0 and marks <= 50):
    print("Fail")
else:
    print("Invaild marks")
