# Pie Chart with Conditional Data 
#Scenario: 
#scores = np.array([40, 60, 80, 30, 90]) 
#Task: 
#● Categorize into: 
#○ Pass (>50) 
#○ Fail (<=50) 
#● Count using NumPy/Pandas 
#● Plot pie chart for Pass vs Fail
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Input data
scores = np.array([40, 60, 80, 30, 90])

# 2. Categorize data using numpy.where
categories = np.where(scores > 50, "Pass", "Fail")

# 3. Create DataFrame and count occurrences
df = pd.DataFrame({"Status": categories})
status_counts = df["Status"].value_counts()

# 4. Plot pie chart
plt.pie(
    status_counts,
    labels=status_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["lightgreen", "coral"],
)

# 5. Add title
plt.title("Proportion of Pass vs Fail Students")

# Show the plot
plt.show()
