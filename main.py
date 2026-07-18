import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
df=pd.read_csv("netflix_titles.csv")
df.head()
df.info()
df.shape
df.isnull().sum()
df=df.drop_duplicates()
df.fillna("Unknown",inplace=True)
df["type"].value_counts().plot(
    kind="bar",
    figsize=(6,4),
    title="Movies vs TV Shows"
)
plt.show()

top=df["country"].value_counts().head(10)
top.plot(kind="bar")
plt.title("Top 10 Countries")
plt.show()

df["release_year"].value_counts().sort_index().plot(figsize=(15,5))
plt.title("Netflix Release by years")
plt.show()

df["rating"].value_counts().plot(kind="bar")
plt.title("Content Ratting")
plt.show()