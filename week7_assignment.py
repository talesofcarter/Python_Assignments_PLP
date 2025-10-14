# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Create a DataFrame from the dataset
# 'iris.data' contains the feature values, and 'iris.feature_names' are the column names
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add the target (species) column to the DataFrame
# The target values are numerical, so we map them to their corresponding species names
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nData types and non-null counts:")
print(df.info())

# Check for any missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Compute basic statistics for numerical columns
print("Basic statistics of the numerical columns:")
print(df.describe())

# Group the data by species and compute the mean of numerical columns
print("\nMean of numerical columns grouped by species:")
print(df.groupby("species").mean())

# Identify interesting findings
print("\nFindings:")
print(
    "1. Setosa species generally has the smallest sepal and petal measurements compared to Versicolor and Virginica."
)
print("2. Virginica species has the largest average sepal and petal lengths.")
print(
    "3. There's a clear difference in the average petal length among the three species, with Setosa having the smallest and Virginica the largest."
)


# Set a style for the plots using seaborn
sns.set_style("whitegrid")

# Create a line chart
plt.figure(figsize=(10, 6))
df["sepal length (cm)"].plot(title="Sepal Length Trend Across the Dataset")
plt.xlabel("Observation Index")
plt.ylabel("Sepal Length (cm)")
plt.show()


# Create a bar chart of average petal length by species
plt.figure(figsize=(8, 6))
species_petal_length = df.groupby("species")["petal length (cm)"].mean()
species_petal_length.plot(kind="bar", color=["skyblue", "salmon", "lightgreen"])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.xticks(rotation=0)  # Rotate x-axis labels for readability
plt.show()


# Create a histogram of petal width
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x="petal width (cm)", bins=10, kde=True)
plt.title("Distribution of Petal Width")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Create a scatter plot of sepal length vs. petal length, colored by species
plt.figure(figsize=(10, 8))
sns.scatterplot(
    x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, s=100
)
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()
