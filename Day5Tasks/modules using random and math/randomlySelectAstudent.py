Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q: Write a program that uses random.choice() to randomly select a student from a list and display:
import random
students=["vin","tony","rah","kar","sam"]
selected_student= random.choice(students)
print("The selected student for the presentation is :{selected_student}")
The selected student for the presentation is :{selected_student}
print(f"student:{selected_student}")
student:vin
print(f"The selected student for the presentation is:{selected_student}")
The selected student for the presentation is:vin
