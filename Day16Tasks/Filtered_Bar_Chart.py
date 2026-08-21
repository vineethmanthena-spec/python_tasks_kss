#Filtered Bar Chart 
#Scenario: 
#marks = np.array([45, 80, 60, 30, 90]) 
#names = ["A", "B", "C", "D", "E"] 
#Task: 
#● Convert to DataFrame 
#● Filter students with marks > 50 
#● Plot bar chart only for filtered students
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Input data
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

# 2. Convert to DataFrame
df = pd.DataFrame({"Name": names, "Marks": marks})

# 3. Filter students with marks > 50 (Filters out A and D)
filtered_df = df[df["Marks"] > 50]

# 4. Plot bar chart only for filtered students
plt.bar(
    filtered_df["Name"],
    filtered_df["Marks"],
    color=["gold", "lightgreen", "coral"],
)

# 5. Add labels and title
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Scoring Above 50 Marks")

# Show the plot
plt.show()
