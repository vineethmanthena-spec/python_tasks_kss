# Student Score Processor 
#Scenario: 
#A teacher stores student names and marks in a list of tuples. 
#Task: 
#● Convert data into a dictionary 
#● Use a loop + condition to find students scoring above 50 
#● Use math module to calculate average 
#● Store results in a text file

import math

student_tuples = [
    ("Alice", 85),
    ("Bob", 42),
    ("Charlie", 78),
    ("David", 49),
    ("Eva", 92)
]

student_dict = dict(student_tuples)

high_scorers = {}
for name, score in student_dict.items():
    if score > 50:
        high_scorers[name] = score

total_marks = math.fsum(student_dict.values())
average_score = total_marks / len(student_dict)

with open("student_results.txt", "w") as file:
    file.write("=== STUDENT SCORE REPORT ===\n\n")
    file.write(f"Class Average Score: {average_score:.2f}\n\n")
    file.write("Students Scoring Above 50:\n")
    for name, score in high_scorers.items():
        file.write(f"- {name}: {score}\n")

print("Data processed and student_results.txt generated successfully!")
