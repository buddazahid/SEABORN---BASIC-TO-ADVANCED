# ========================================================
#           SEABORN - BASIC TO ADVANCED
# ========================================================

# Seaborn is a Python visualization library
# built on top of Matplotlib.

# Install:
# pip install seaborn matplotlib pandas

# ========================================================
#                   IMPORT LIBRARIES
# ========================================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ========================================================
#                   LOAD DATASET
# ========================================================

# Built-in seaborn dataset
data = sns.load_dataset("tips")

print(data.head())

# ========================================================
#                   BASIC LINE PLOT
# ========================================================

plt.figure(figsize=(6,4))

sns.lineplot(x=[1,2,3,4], y=[10,20,15,25])

plt.title("Line Plot")

plt.show()

# ========================================================
#                   BAR PLOT
# ========================================================

plt.figure(figsize=(6,4))

sns.barplot(x="day", y="total_bill", data=data)

plt.title("Bar Plot")

plt.show()

# ========================================================
#                   SCATTER PLOT
# ========================================================

plt.figure(figsize=(6,4))

sns.scatterplot(
    x="total_bill",
    y="tip",
    hue="sex",
    data=data
)

plt.title("Scatter Plot")

plt.show()

# ========================================================
#                   HISTOGRAM
# ========================================================

plt.figure(figsize=(6,4))

sns.histplot(data["total_bill"], bins=10)

plt.title("Histogram")

plt.show()

# ========================================================
#                   KDE PLOT
# ========================================================

plt.figure(figsize=(6,4))

sns.kdeplot(data["tip"], fill=True)

plt.title("KDE Plot")

plt.show()

# ========================================================
#                   BOX PLOT
# ========================================================

plt.figure(figsize=(6,4))

sns.boxplot(
    x="day",
    y="total_bill",
    data=data
)

plt.title("Box Plot")

plt.show()

# ========================================================
#                   VIOLIN PLOT
# ========================================================

plt.figure(figsize=(6,4))

sns.violinplot(
    x="day",
    y="tip",
    data=data
)

plt.title("Violin Plot")

plt.show()

# ========================================================
#                   COUNT PLOT
# ========================================================

plt.figure(figsize=(6,4))

sns.countplot(x="sex", data=data)

plt.title("Count Plot")

plt.show()

# ========================================================
#                   HEATMAP
# ========================================================

# Create correlation matrix
corr = data.corr(numeric_only=True)

plt.figure(figsize=(6,4))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Heatmap")

plt.show()

# ========================================================
#                   PAIR PLOT
# ========================================================

sns.pairplot(data, hue="sex")

plt.show()

# ========================================================
#                   JOINT PLOT
# ========================================================

sns.jointplot(
    x="total_bill",
    y="tip",
    data=data,
    kind="scatter"
)

plt.show()

# ========================================================
#                   ADVANCED STYLE
# ========================================================

# Themes:
# darkgrid
# whitegrid
# dark
# white
# ticks

sns.set_style("darkgrid")

plt.figure(figsize=(6,4))

sns.barplot(
    x="day",
    y="tip",
    data=data,
    palette="Set2"
)

plt.title("Styled Bar Plot")

plt.show()

# ========================================================
#                   CUSTOM DATAFRAME
# ========================================================

student = pd.DataFrame({

    "Name": ["Zahid", "Rahul", "Aman", "Sara"],

    "Marks": [85, 90, 78, 88],

    "Age": [21, 22, 20, 21]
})

print(student)

# ========================================================
#               CUSTOM DATA VISUALIZATION
# ========================================================

plt.figure(figsize=(6,4))

sns.barplot(
    x="Name",
    y="Marks",
    data=student
)

plt.title("Student Marks")

plt.show()

# ========================================================
#                   RANDOM DATA
# ========================================================

random_data = np.random.randn(100)

plt.figure(figsize=(6,4))

sns.histplot(random_data, kde=True)

plt.title("Random Data Distribution")

plt.show()

# ========================================================
#                   PROGRAM END
# ========================================================

# Seaborn is mainly used for:
# - Data Visualization
# - Data Analysis
# - Machine Learning Graphs
# - Statistical Charts

# Popular Seaborn Plots:
# 1. lineplot()
# 2. scatterplot()
# 3. barplot()
# 4. histplot()
# 5. heatmap()
# 6. pairplot()
# 7. boxplot()
# 8. violinplot()

# ========================================================