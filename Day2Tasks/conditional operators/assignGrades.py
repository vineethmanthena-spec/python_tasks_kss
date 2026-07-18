Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program to assign grades based on marks (for example: A, B, C, Fail)
marks=77
if marks >= 90:
            grade = "A"
elif marks >= 80:
            grade = "B"
elif marks >= 70:
            grade = "C"
elif marks >= 60:
            grade = "D"
else:
            grade = "Fail"

            
print(f"The assigned grade is: {grade}")
The assigned grade is: C
