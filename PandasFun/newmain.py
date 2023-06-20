import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Part 1 - Read and Print Data (10 points)
data_file = "song 10.csv"
df = pd.read_csv(data_file)
print(f"Number of rows and columns in data: {df.shape}")

# Part 2 - Print Row info (20 points)
row_number = int(input("Enter row number: "))
print(df.iloc[row_number])

# Part 3 - Grouping Data (5 points)
grouped_data = df.groupby("instrumentalness")

# Printing Joined DataFrames info (5 points)
print(grouped_data.describe())

# Handling Missing Values (5 points)
df.fillna(value='Replace_value', inplace=True)

# Top 5 Artists with maximum Clicks/Failures (20 points)
top_artists = df.groupby("chorus_hit")["instrumentalness"].sum().nlargest(5)
print("Top 5 artists with maximum failures/clicks:")
print(top_artists)

# Part 4 - Grouping by Clicks/Failures and Printing mean/standard deviation (10 points)
grouped_by_clicks_failures = df.groupby("instrumentalness")
print("Mean and Standard Deviation grouped by failures/clicks:")
print(grouped_by_clicks_failures.agg({"duration_ms": ["mean", "std"]}))

# Clicks/Failures histogram (10 points)
plt.figure()
sns.histplot(data=df, x="instrumentalness", kde=True)
plt.title("Histogram of Failures/Clicks")
plt.xlabel("Failures/Clicks")
plt.ylabel("Frequency")
plt.show()

# Genre bar plot (5 points)
plt.figure()
sns.countplot(x="chorus_hit", data=df, order=df.time_signature.value_counts().index)
plt.title("Count of Songs by Genre")
plt.xlabel("Genre")
plt.xticks(rotation=45)
plt.ylabel("Count")
plt.show()
