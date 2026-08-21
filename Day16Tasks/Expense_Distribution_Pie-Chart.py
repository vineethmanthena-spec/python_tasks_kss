# Expense Distribution Pie Chart 
#Scenario: 
#Monthly expenses: 
#expenses = np.array([500, 300, 200]) 
#labels = ["Food", "Rent", "Travel"] 
#Task: 
#● Create a pie chart 
#● Show percentage distribution
import matplotlib.pyplot as plt
import numpy as np

# Given data
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

# 1. Create a pie chart & 2. Show percentage distribution
# autopct='%1.1f%%' formats and displays the percentage on each wedge
plt.pie(
    expenses,
    labels=labels,
    autopct="%1.1f%%",
    startangle=140,
    colors=["#ff9999", "#66b3ff", "#99ff99"],
)

plt.title("Monthly Expense Distribution")

# Display the plot
plt.show()
