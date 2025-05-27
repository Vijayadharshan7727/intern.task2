import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("Titanic-Dataset.csv")
print("First 5 Rows of the Dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Cabin'].fillna('Unknown', inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Fare'])
plt.title("Boxplot of Fare")
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x='Survived', data=df)
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare']])
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age vs Survival")
plt.show()

plt.figure(figsize=(6, 4))
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title("Survival Rate by Passenger Class")
plt.show()

plt.figure(figsize=(6, 6))
df['Embarked'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, shadow=True)
plt.title("Port of Embarkation Distribution")
plt.ylabel("")
plt.show()

print("\nInferences:")
print("- Most passengers were in the age group of 20–40.")
print("- Passengers in Pclass 1 had higher survival rates.")
print("- There are some outliers in Fare values (as seen in the boxplot).")
print("- The correlation matrix shows Fare and Pclass are moderately related to Survival.")
