# Temperature Monitoring System 
#Scenario: 
#temps = np.array([28, 30, 32, 35, 33, 31, 29]) 
#days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
#Task: 
#● Create DataFrame 
#● Plot: 
#○ Line graph → daily temperature trend 
#○ Bar chart → day-wise temperature 
#○ Pie chart → proportion of high (>30) vs low temps 
#○ Histogram → temperature frequency 
#○ Scatter plot → day index vs temperature
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Structural array ingestion and DataFrame compilation
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
df = pd.DataFrame({"Day": days, "Temperature": temps})

# 2. Build multi-chart dashboard workspace
fig, axes = plt.subplots(3, 2, figsize=(10, 12))
axes = axes.flatten()

# Line Graph → Daily trend line
axes[0].plot(df["Day"], df["Temperature"], marker="o", color="#d62728", linewidth=2)
axes[0].set_title("Daily Temperature Trend")
axes[0].set_ylabel("Temp (°C)")
axes[0].grid(True, linestyle="--", alpha=0.5)

# Bar Chart → Day-wise comparative columns
axes[1].bar(df["Day"], df["Temperature"], color="#ff7f0e", edgecolor="black")
axes[1].set_title("Day-wise Temperature")
axes[1].set_ylabel("Temp (°C)")

# Pie Chart → Threshold logic breakdown (>30°C vs <=30°C)
high_temp = sum(df["Temperature"] > 30)
low_temp = sum(df["Temperature"] <= 30)
axes[2].pie([high_temp, low_temp], labels=["High (>30°C)", "Low/Mod (≤30°C)"], 
        autopct="%1.1f%%", colors=["#d62728", "#1f77b4"], startangle=90)
axes[2].set_title("Proportion of High vs Low Temps")

# Histogram → Climate zone distribution frequency
axes[3].hist(df["Temperature"], bins=4, color="#2ca02c", edgecolor="black")
axes[3].set_title("Temperature Frequency")
axes[3].set_xlabel("Temp Range (°C)")

# Scatter Plot → Coordinate sequence index map
axes[4].scatter(df.index, df["Temperature"], color="#9467bd", s=100)
for i, txt in enumerate(df["Day"]):
    axes[4].annotate(txt, (df.index[i], df["Temperature"][i]), textcoords="offset points", xytext=(0,10), ha='center')
axes[4].set_title("Day Index vs Temperature")
axes[4].set_xlabel("Day Index")

# Strip extra subplot space and render
fig.delaxes(axes[5])
plt.tight_layout()
plt.show()
