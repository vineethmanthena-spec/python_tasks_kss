#Data Cleaning + Visualization 
#Scenario: 
#data = np.array([100, np.nan, 200, 150, np.nan, 300]) 
#Task: 
#1. Convert to Pandas Series 
#2. Replace NaN with mean 
#3. Plot: 
#○ Line graph of cleaned data 
#○ Bar chart of values > average
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Create data array with missing values
data = np.array([100, np.nan, 200, 150, np.nan, 300])

# 2. Convert to Pandas Series
series = pd.Series(data)

# 3. Replace NaN values with the mean of the series
# The mean of [100, 200, 150, 300] is 187.5
mean_value = series.mean()
cleaned_series = series.fillna(mean_value)

# 4. Filter values that are strictly greater than the overall average (187.5)
# This keeps index 2 (200) and index 5 (300)
above_average = cleaned_series[cleaned_series > mean_value]

# 5. Create a 1x2 subplot layout for visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- Plot 1: Line Graph of Cleaned Data ---
axes[0].plot(
    cleaned_series.index,
    cleaned_series.values,
    marker="o",
    color="blue",
    linewidth=2,
)
axes[0].set_title("Cleaned Data Trend (NaN Replaced with Mean)")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Values")
axes[0].grid(True, linestyle="--", alpha=0.6)

# --- Plot 2: Bar Chart of Values > Average ---
axes[1].bar(
    above_average.index.astype(str), above_average.values, color="lightgreen"
)
axes[1].axhline(
    mean_value,
    color="red",
    linestyle="--",
    label=f"Mean ({mean_value:.1f})",
)
axes[1].set_title("Values Greater Than Average")
axes[1].set_xlabel("Original Index")
axes[1].set_ylabel("Values")
axes[1].legend()

# Display the dashboard
plt.tight_layout()
plt.show()
