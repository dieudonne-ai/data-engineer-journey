import pandas as pd

df = pd.read_csv("data/students.csv")

df["score"] = pd.to_numeric(df["score"], errors="coerce")

#df_clean = df.dropna() #this will drop all rows with NaN values, which may not be desirable if we want to keep some of the data

average_score = df["score"].mean()
df["score"] = df["score"].fillna(average_score) #this will fill NaN values with the average score

print(df.duplicated()) #this will show which rows are duplicates
df = df.drop_duplicates() #this will remove duplicate rows

df = df[(df["score"] >= 0) & (df["score"] <=20)] #this will filter out rows where the score is less than 0 or greater than 20

df.to_csv("clean_data/students_clean.csv", index=False) #this will save the cleaned data to a new CSV file without the index column
