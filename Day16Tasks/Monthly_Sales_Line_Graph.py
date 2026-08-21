#Monthly Sales Line Graph 
#Scenario: 
#A shop records monthly sales: 
#sales = np.array([100, 150, 200, 250, 300]) 
#months = ["Jan", "Feb", "Mar", "Apr", "May"] 
#Task: 
#● Convert data into a Pandas DataFrame 
#● Plot a line graph 
#● Label X-axis as months and Y-axis as sales
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Given data
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

# 1. Convert data into a Pandas DataFrame
df = pd.DataFrame({"Month": months, "Sales": sales})

# 2. Plot a line graph
plt.plot(df["Month"], df["Sales"], marker="o", color="b", linestyle="-")

# 3. Label X-axis and Y-axis
plt.xlabel("months")
plt.ylabel("sales")
plt.title("Monthly Sales Performance")

# Display the plot
plt.grid(True)
plt.show()
