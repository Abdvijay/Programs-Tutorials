marks = int(input("Enter the marks : "))
if marks >= 90:
    print("Grade is O")
elif marks >= 80 and marks < 90 :
    print("Grade is A+")
elif marks >= 70 and marks < 80 :
    print("Grade is A")
elif marks >= 60 and marks < 70 :
    print("Grade is B")
elif marks >=50 and marks < 60 :
    print("Grade is C")
else:
    print("Fail in the Exam")

"""
PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\If-Else-Programs> python GradeSystemMark.py
Enter the marks : 54
Grade is C
PS C:\Users\My_Sowriyam\OneDrive\Desktop\Programs-Tutorials\Python\If-Else-Programs> python GradeSystemMark.py
Enter the marks : 93
Grade is O

"""