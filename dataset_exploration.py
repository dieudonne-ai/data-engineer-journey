import pandas as pd

df = pd.read_csv("data/students.csv")

df["score"] = pd.to_numeric(df["score"], errors="coerce")

#print(df.shape) #this will print the number of rows and columns in the dataset
#print(df.info()) #this will print the data types of each column and the number of non-null values
#print(df.describe()) #this will print summary statistics for the numeric columns in the dataset

#print(df.isnull().sum()) #this will print the number of missing values in each column
#print(df["score"].unique())

print(df["score"].isna().sum())