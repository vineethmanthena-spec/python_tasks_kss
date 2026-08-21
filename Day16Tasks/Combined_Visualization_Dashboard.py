# Combined Visualization Dashboard 
#Scenario: 
#sales = np.array([100, 200, 150, 300]) 
#products = ["A", "B", "C", "D"] 
#Task: 
#● Create DataFrame 
#● Plot: 
#○ Line graph (trend) 
#○ Bar chart (comparison) 
#○ Pie chart (distribution) 
#● Show all in single figure (subplots)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Input data
sales = np.array([100, 200, 150, 300])  # Added data
products = ["A", "B", "C", "D"]

# 2. Create DataFrame
df = pd.DataFrame({"Product": products, "Sales": sales})

# 3. Create a single figure with 3 subplots side-by-side
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# --- Plot 1: Line Graph (Trend) ---
axes[0].plot(
    df["Product"], df["Sales"], marker="o", color="blue", linewidth=2
)
axes[0].set_title("Sales Trend")
axes[0].set_xlabel("Product")
axes[0].set_ylabel("Sales Units")
axes[0].grid(True, linestyle="--", alpha=0.6)

# --- Plot 2: Bar Chart (Comparison) ---
axes[1].bar(
    df["Product"], df["Sales"], color=["gold", "lightgreen", "coral", "skyblue"]
)
axes[1].set_title("Product Comparison")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Sales Units")

# --- Plot 3: Pie Chart (Distribution) ---
axes[2].pie(
    df["Sales"],
    labels=df["Product"],
    autopct="%1.1f%%",
    startangle=140,
    colors=["gold", "lightgreen", "coral", "skyblue"],
)
axes[2].set_title("Sales Distribution")

# 4. Clean up layout structure and display
plt.tight_layout()
plt.show()
