# Multi-Line Graph for Sales Comparison 
#Scenario: 
#data = { 
#"Month": ["Jan", "Feb", "Mar"], 
#"Store_A": [100, 150, 200], 
#"Store_B": [90, 140, 210] 
#} 
#Task: 
#● Create DataFrame 
#● Plot two line graphs on same plot 
#● Add legend
import matplotlib.pyplot as plt
import pandas as pd

# 1. Create the data dictionary
data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A":[100,200,300],
    "Store_B":[90,70,80]
}

# 2. Create DataFrame
df = pd.DataFrame(data)

# 3. Plot two line graphs on the same plot
plt.plot(df["Month"], df["Store_A"], marker="o", label="Store A", color="blue")
plt.plot(
    df["Month"], df["Store_B"], marker="s", label="Store B", color="orange"
)

# 4. Add labels, title, and legend
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Comparison: Store A vs Store B")
plt.legend()  # Displays the labels 'Store A' and 'Store B'

# Show the plot
plt.show()
