# Monthly Sales Analysis 
#Scenario: 
#sales = np.array([100, 150, 200, 180, 220, 300]) 
#months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] 
#Task: 
#● Create DataFrame 
#● Plot: 
#○ Line graph → sales trend 
#○ Bar chart → month-wise comparison 
#○ Pie chart → contribution of each month 
#○ Histogram → frequency of sales values 
#○ Scatter plot → month index vs sales

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Initialize data and create DataFrame
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
df = pd.DataFrame({"Month": months, "Sales": sales})

# 2. Configure multi-plot dashboard layout
fig, axes = plt.subplots(3, 2, figsize=(11, 13))
axes = axes.flatten()

# Line Graph
axes[0].plot(df["Month"], df["Sales"], marker="o", color="#1f77b4", linewidth=2)
axes[0].set_title("Line Graph: Sales Trend")
axes[0].grid(True, linestyle="--", alpha=0.6)

# Bar Chart
axes[1].bar(df["Month"], df["Sales"], color="#2ca02c", edgecolor="black")
axes[1].set_title("Bar Chart: Month-wise Comparison")

# Pie Chart
axes[2].pie(df["Sales"], labels=df["Month"], autopct="%1.1f%%", startangle=90)
axes[2].set_title("Pie Chart: Monthly Contribution")

# Histogram
axes[3].hist(df["Sales"], bins=5, color="#bcbd22", edgecolor="black")
axes[3].set_title("Histogram: Frequency of Sales Values")

# Scatter Plot
axes[4].scatter(df.index, df["Sales"], color="#d62728", s=100)
axes[4].set_title("Scatter Plot: Month Index vs Sales")
axes[4].set_xticks(df.index)

# Clean empty quadrant and render
fig.delaxes(axes[5])
plt.tight_layout()
plt.show()
