import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
df = pd.read_csv("scottish_hills.csv")
df["Height"] = pd.to_numeric(df["Height"], errors='coerce')
lat_mid = df["Latitude"].median()
lon_mid = df["Longitude"].median()

def assign_region(row):
    lat = row["Latitude"]
    lon = row["Longitude"]
    
    if lat >= lat_mid and lon >= lon_mid:
        return "North-East"
    elif lat >= lat_mid and lon < lon_mid:
        return "North-West"
    elif lat < lat_mid and lon >= lon_mid:
        return "South-East"
    else:
        return "South-West"

df["Region"] = df.apply(assign_region, axis=1)
df["Height"] = df["Height"].fillna(df["Height"].mean())

# Fill Region with mode
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])
print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

#SCENARIO 2: Line Graph (Score Trend) + Save
data = df[['Hill Name', 'Height']]
data_10 = data.head(10)
height_array = np.array(data_10['Height'])
plt.figure()
plt.plot(range(10), height_array, marker='o')
plt.title("Height Variation of First 10 Hills")
plt.xlabel("Index (0–9)")
plt.ylabel("Height")
plt.tight_layout()
plt.savefig("hill_heights_line.png")
plt.show()
#SCENARIO 3: Filtering + Bar Chart + Save
tall_hills = df[df['Height'] > 900]
region_counts = tall_hills['Region'].value_counts()
top_regions = region_counts.head()
regions_array = np.array(top_regions.index)
counts_array = np.array(top_regions.values)
plt.figure()
plt.bar(regions_array, counts_array)
plt.title("Number of Tall Hills (>900m) per Region")
plt.xlabel("Region")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("tall_hills_bar.png")
plt.show()

#SCENARIO 4: Pie Chart (Region Distribution) + Save
region_counts = df["Region"].value_counts()
top_regions = region_counts.head(5)
labels = top_regions.index
values = top_regions.values
plt.figure(figsize=(10, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Hills by Region")
plt.tight_layout()
plt.savefig("region_distribution.png")
plt.show()

#SCENARIO 5: Advanced Analysis + Multiple Graphs
def height_category(h):
    if h >= 1000:
        return "Very High"
    elif h >= 800:
        return "High"
    else:
        return "Moderate"

df["Height_Category"] = df["Height"].apply(height_category)
height_array = np.array(df["Height"])

height_diff = np.diff(height_array)

print("\nFirst 10 Height Differences:")
print(height_diff[:10])
 #1. Line Graph (Height Trend)
plt.figure()
plt.plot(range(len(height_array)), height_array)
plt.title("Height Trend of All Hills")
plt.xlabel("Index")
plt.ylabel("Height")
plt.tight_layout()
plt.savefig("height_trend.png")
plt.show()

category_region = pd.crosstab(df["Region"], df["Height_Category"])
# 🔹 2. Stacked Bar Chart (Category per Region)

category_region.plot(kind="bar", stacked=True)
plt.title("Height Category Distribution per Region")
plt.xlabel("Region")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("height_category_stacked.png")
plt.show()
 #3. Histogram (Height Distribution)
plt.figure()
plt.hist(df["Height"], bins=10, edgecolor = 'black')
plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("height_histogram.png")
plt.show()
# PART 4: INSIGHTS
# Tallest region
tallest_region = df.groupby("Region")["Height"].mean().idxmax()
# Most common category
common_category = df["Height_Category"].value_counts().idxmax()

print("\nInsights We have Got are:")
print("Tallest Region (avg height):", tallest_region)
print("Most Common Height Category:", common_category)


