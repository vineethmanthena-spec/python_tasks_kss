#Q:Student Attendance Record .
#A teacher wants to store student attendance in a file named attendance.txt. Write a 
#Python program that takes a student name as input and appends it to the file. Then 
#display the contents of the file. 

with open("attendance.txt", "a") as file:
    student_name = input("Enter student name: ")
    file.write(student_name + "\n")

print("\n--- Current Attendance List ---")

with open("attendance.txt", "r") as file:
    content = file.read()
    print(content)
