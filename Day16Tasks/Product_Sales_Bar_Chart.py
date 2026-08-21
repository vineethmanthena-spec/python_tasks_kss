# Product Sales Bar Chart 
#Scenario: 
#products = ["Pen", "Book", "Pencil"] 
#sales = np.array([50, 80, 40]) 
#Task: 
#● Create DataFrame 
#● Plot bar chart 
#● Add labels and title 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Create the data
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

# 2. Create DataFrame
df = pd.DataFrame({"Product": products, "Sales": sales})

# 3. Plot bar chart
plt.bar(df["Product"], df["Sales"], color=["skyblue", "lightgreen", "salmon"])

# 4. Add labels and title
plt.xlabel("Products")
plt.ylabel("Sales Units")
plt.title("Product Sales Comparison")

# Show the plot
plt.show()
