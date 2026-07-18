Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q: Write a program to find the student with the highest marks from a dictionary.
student_marks = {
    'vin': 85,
    'tony': 92,
    'mah': 78,
    }
max(student_marks,key=student_marks.get)
'tony'
