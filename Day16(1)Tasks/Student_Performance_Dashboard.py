# Student Performance Dashboard 
#Scenario: 
#A school records marks of students in one subject: 
#marks = np.array([45, 67, 89, 56, 72, 91, 38]) 
#students = ["A", "B", "C", "D", "E", "F", "G"] 
#Task: 
#● Convert to Pandas DataFrame 
#● Plot: 
#○ Line graph → trend of marks 
#○ Bar chart → student vs marks 
#○ Pie chart → Pass (>50) vs Fail 
#○ Histogram → distribution of marks 
#○ Scatter plot → index vs marks
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Convert to Pandas DataFrame
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]
df = pd.DataFrame({"Student": students, "Marks": marks})

# 2. Plotting Dashboard
fig, axes = plt.subplots(3, 2, figsize=(12, 14))
axes = axes.flatten()

# Line Graph
axes[0].plot(df["Student"], df["Marks"], marker="o", color="b")
axes[0].set_title("Line Graph: Trend of Marks")

# Bar Chart
axes[1].bar(df["Student"], df["Marks"], color="skyblue", edgecolor="black")
axes[1].axhline(y=50, color="r", linestyle="--", label="Pass Line")
axes[1].set_title("Bar Chart: Student vs Marks")
axes[1].legend()

# Pie Chart
pass_count = sum(df["Marks"] >= 50)
fail_count = sum(df["Marks"] < 50)
axes[2].pie(
    [pass_count, fail_count],
    labels=["Pass", "Fail"],
    autopct="%1.1f%%",
    colors=["green", "red"],
)
axes[2].set_title("Pie Chart: Pass vs Fail")

# Histogram
axes[3].hist(df["Marks"], bins=5, color="purple", edgecolor="black")
axes[3].set_title("Histogram: Distribution of Marks")

# Scatter Plot
axes[4].scatter(df.index, df["Marks"], color="darkorange", s=100)
axes[4].set_title("Scatter Plot: Index vs Marks")

# Clean up layout
fig.delaxes(axes[5])
plt.tight_layout()
plt.show()
