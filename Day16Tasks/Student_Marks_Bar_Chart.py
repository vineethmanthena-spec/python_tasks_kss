# Student Marks Bar Chart 
#Scenario: 
#Marks of students: 
#names = ["A", "B", "C", "D"] 
#marks = np.array([70, 85, 60, 90]) 
#Task: 
#● Create a DataFrame 
#● Plot a bar graph 
#● Show student names on X-axis
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Given data
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

# 1. Create a DataFrame
df = pd.DataFrame({"Student": names, "Marks": marks})

# 2. Plot a bar graph
plt.bar(df["Student"], df["Marks"], color="skyblue", edgecolor="black")

# 3. Show student names on X-axis (and label the axes)
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.title("Student Marks Comparison")

# Display the plot
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
