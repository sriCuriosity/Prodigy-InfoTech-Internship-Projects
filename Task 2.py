# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the training dataset
train_df = pd.read_csv("D:\\Sri Nithilan\\Documents\\InfoProdigy\\titanic\\train.csv")

# Load the testing dataset
test_df = pd.read_csv("D:\\Sri Nithilan\\Documents\\InfoProdigy\\titanic\\test.csv")

# Load the gender submission dataset
gender_submission_df = pd.read_csv("D:\\Sri Nithilan\\Documents\\InfoProdigy\\titanic\\gender_submission.csv")

# Data Cleaning
# Check for missing values
print("Missing values in train dataset: \n", train_df.isnull().sum())
print("Missing values in test dataset: \n", test_df.isnull().sum())
print("Missing values in gender submission dataset: \n", gender_submission_df.isnull().sum())

# Fill missing values with mean
train_df['Age'].fillna(train_df['Age'].mean(), inplace=True)
test_df['Age'].fillna(test_df['Age'].mean(), inplace=True)
test_df['Fare'].fillna(test_df['Fare'].mean(), inplace=True)

# Exploratory Data Analysis (EDA)
# 1. Distribution of Ages
plt.figure(figsize=(10, 6))
sns.histplot(train_df['Age'], bins=20, kde=True)
plt.title("Distribution of Ages")
plt.show()

# 2. Survival Rate by Sex
plt.figure(figsize=(8, 6))
sns.countplot(x='Sex', hue='Survived', data=train_df)
plt.title("Survival Rate by Sex")
plt.show()

# 3. Survival Rate by Pclass
plt.figure(figsize=(8, 6))
sns.countplot(x='Pclass', hue='Survived', data=train_df)
plt.title("Survival Rate by Pclass")
plt.show()

# 4. Survival Rate by Embarked
plt.figure(figsize=(8, 6))
sns.countplot(x='Embarked', hue='Survived', data=train_df)
plt.title("Survival Rate by Embarked")
plt.show()

# 5. Correlation between Features
plt.figure(figsize=(10, 8))
sns.heatmap(train_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation between Features")
plt.show()

# 6. Distribution of Fares
plt.figure(figsize=(10, 6))
sns.boxplot(train_df['Fare'])
plt.title("Distribution of Fares")
plt.show()

# 7. Survival Rate by SibSp and Parch
plt.figure(figsize=(10, 6))
sns.scatterplot(x='SibSp', y='Parch', hue='Survived', data=train_df)
plt.title("Survival Rate by SibSp and Parch")
plt.show()

# 8. Survival Rate by Age and Sex
plt.figure(figsize=(10, 6))
sns.violinplot(x='Sex', y='Age', hue='Survived', data=train_df, split=True)
plt.title("Survival Rate by Age and Sex")
plt.show()