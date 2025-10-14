import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re

# Part 1: Data Loading and Basic Exploration
# Load the sample metadata
df = pd.read_csv("metadata.csv")

# Examine the first few rows and structure
print("First 5 rows:")
print(df.head())
print("\nDataFrame info:")
print(df.info())
print("\nDimensions (rows, columns):", df.shape)
print("\nData types:")
print(df.dtypes)

# Check for missing values in important columns
important_cols = ["title", "abstract", "publish_time", "authors", "journal", "source_x"]
print("\nMissing values:")
print(df[important_cols].isnull().sum())

# Basic statistics for numerical columns (none in this sample, but included for completeness)
print("\nBasic statistics:")
print(df.describe())


# Part 2: Data Cleaning and Preparation
# Handle missing data (sample has none, but included for robustness)
df_clean = df.dropna(subset=["title", "abstract"])

# Convert publish_time to datetime
df_clean["publish_time"] = pd.to_datetime(df_clean["publish_time"], errors="coerce")

# Extract year from publication date
df_clean["year"] = df_clean["publish_time"].dt.year

# Create abstract word count column
df_clean["abstract_word_count"] = df_clean["abstract"].apply(
    lambda x: len(str(x).split())
)

print("\nCleaned DataFrame shape:", df_clean.shape)
print("\nMissing values after cleaning:")
print(df_clean[important_cols].isnull().sum())


# Part 3: Data Analysis and Visualization
# Count papers by publication year
year_counts = df_clean["year"].value_counts().sort_index()
print("\nPapers by year:")
print(year_counts)

# Identify top journals
top_journals = df_clean["journal"].value_counts().head(10)
print("\nTop 10 journals:")
print(top_journals)


# Most frequent words in titles
def get_word_freq(text_series):
    all_text = " ".join(text_series.fillna("").str.lower())
    words = re.findall(r"\w+", all_text)
    return Counter(words)


title_word_freq = get_word_freq(df_clean["title"])
most_common_titles = title_word_freq.most_common(20)
print("\nMost frequent words in titles:")
print(most_common_titles)

# Plot number of publications over time
plt.figure(figsize=(10, 6))
sns.barplot(x=year_counts.index, y=year_counts.values)
plt.title("Number of Publications by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()  # Display the plot

# Bar chart of top publishing journals
plt.figure(figsize=(10, 6))
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title("Top 10 Publishing Journals")
plt.xlabel("Count")
plt.ylabel("Journal")
plt.show()  # Display the plot

# Generate word cloud of paper titles
all_titles = " ".join(df_clean["title"].fillna(""))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
    all_titles
)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Paper Titles")
plt.show()  # Display the plot

# Plot distribution of paper counts by source
source_counts = df_clean["source_x"].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=source_counts.values, y=source_counts.index)
plt.title("Distribution of Papers by Source")
plt.xlabel("Count")
plt.ylabel("Source")
plt.show()  # Display the plot
