#Advanced Simulation System 
#Scenario: 
#Simulate exam results and generate reports. 
#Task: 
#● Generate random marks using random 
#● Store in NumPy array 
#● Convert to Pandas DataFrame 
#● Use OOP to represent Student 
#● Use conditions + loops to assign grades 
#● Save report to file 
#● Handle errors using try-except 
#● Use math module for statistics
import os
import math
import random
import numpy as np
import pandas as pd

class Student:
    """Object-Oriented representation of a student and their academic performance."""
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        """Uses condition branching blocks to assign structural letter grades."""
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"

def generate_simulation_report(output_filename="generated/exam_report.csv"):
    # Mock data pool
    student_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
    
    # 1. Generate random marks using native random module
    random.seed(42)  # Set seed for reproducible distributions
    raw_scores = [random.randint(50, 100) for _ in range(len(student_names))]
    
    # 2. Store records in an optimized NumPy array
    scores_array = np.array(raw_scores)
    
    # 3. Instantiate domain entities using Object-Oriented Programming (OOP)
    students_list = []
    for idx, name in enumerate(student_names):
        student_id = f"STU{1000 + idx}"
        # Extract individual matrix items from the NumPy array
        individual_score = int(scores_array[idx])
        students_list.append(Student(student_id, name, individual_score))
        
    # 4. Convert simulation records to a structured Pandas DataFrame
    records_dict = {
        "StudentID": [s.student_id for s in students_list],
        "Name": [s.name for s in students_list],
        "Score": [s.score for s in students_list],
        "Grade": [s.grade for s in students_list]
    }
    df_report = pd.DataFrame(records_dict)
    
    # 5. Leverage the native math module to extract key statistics
    extracted_scores = df_report["Score"].tolist()
    sample_size = len(extracted_scores)
    
    mean_score = sum(extracted_scores) / sample_size
    variance = sum((x - mean_score) ** 2 for x in extracted_scores) / sample_size
    
    # Use math.sqrt for precise statistical computations
    standard_deviation = math.sqrt(variance)
    
    print("📊 --- Simulation Statistics Summary ---")
    print(f"Total Cohort Size : {sample_size} Students")
    print(f"Calculated Mean   : {mean_score:.2f}")
    print(f"Standard Deviation: {standard_deviation:.2f}\n")
    
    # 6. Apply protective try-except blocks to secure local file I/O operations
    try:
        # Create output container directory safely
        os.makedirs(os.path.dirname(output_filename), exist_ok=True)
        
        # Write structural dataset out to file storage
        df_report.to_csv(output_filename, index=False)
        print(f"💾 Report safely written to storage file at: '{output_filename}'")
        return df_report
        
    except PermissionError:
        print(f"❌ Critical Error: Permission denied while attempting to write to '{output_filename}'. Close target files.")
    except FileNotFoundError:
        print(f"❌ Critical Error: The directory tree path for '{output_filename}' could not be constructed.")
    except Exception as unexpected_err:
        print(f"❌ An unexpected systemic error occurred during file serialization: {unexpected_err}")

# Execute the simulation engine routine
if __name__ == "__main__":
    generated_dataframe = generate_simulation_report()
    print("\n--- Top Sample Output Data Stream View ---")
    print(generated_dataframe)
