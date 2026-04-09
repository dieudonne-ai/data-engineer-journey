import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_data/students_clean.csv")
df["score"] = pd.to_numeric(df["score"], errors="coerce")

plt.figure(figsize=(8,5))
plt.bar(df["name"], df["score"], color="green")

plt.title("Student Scores")
plt.xlabel("Student Name")
plt.ylabel("Score")

plt.show()


plt.hist(df["score"].dropna(), bins=10, edgecolor="green", color="black")

plt.title("Score Distribution") 
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()