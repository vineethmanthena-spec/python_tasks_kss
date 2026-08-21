# Employee Salary Insights 
#Scenario: 
#salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
#departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"] 
#Task: 
#● Convert into DataFrame 
#● Plot: 
#○ Line graph → salary trend 
#○ Bar chart → department-wise salary comparison 
#○ Pie chart → department distribution 
#○ Histogram → salary distribution 
#○ Scatter plot → index vs salary
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Initialize structural data arrays & create DataFrame
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]
df = pd.DataFrame({"Department": departments, "Salary": salaries})

# Pre-aggregate data for department metrics
dept_salary = df.groupby("Department")["Salary"].mean().reset_index()
dept_counts = df["Department"].value_counts().reset_index()

# 2. Configure structural multi-chart dashboard layout
fig, axes = plt.subplots(3, 2, figsize=(10, 12))
axes = axes.flatten()

# Line Graph → Salary Trend
axes[0].plot(df.index, df["Salary"], marker="o", color="#1f77b4", linewidth=2)
axes[0].set_title("Line Graph: Salary Trend")
axes[0].set_xlabel("Employee Index")

# Bar Chart → Department average comparison
axes[1].bar(dept_salary["Department"], dept_salary["Salary"], color="#2ca02c", edgecolor="black", width=0.5)
axes[1].set_title("Bar Chart: Avg Salary by Department")

# Pie Chart → Departmental distribution breakdown
axes[2].pie(dept_counts["count"], labels=dept_counts["Department"], autopct="%1.1f%%", startangle=140)
axes[2].set_title("Pie Chart: Department Distribution")

# Histogram → Structural distribution ranges
axes[3].hist(df["Salary"], bins=4, color="#9467bd", edgecolor="black")
axes[3].set_title("Histogram: Salary Distribution")

# Scatter Plot → Index coordinate matching vs Salary
axes[4].scatter(df.index, df["Salary"], color="#d62728", s=100)
for i, txt in enumerate(df["Department"]):
    axes[4].annotate(txt, (df.index[i], df["Salary"][i]), textcoords="offset points", xytext=(0,10), ha='center')
axes[4].set_title("Scatter Plot: Index vs Salary")

# Remove extra quadrant grid & plot
fig.delaxes(axes[5])
plt.tight_layout()
plt.show()
