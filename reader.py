import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_data/grade_summary.csv")
df["mean"] = pd.to_numeric(df["mean"], errors="coerce")

print(df.shape)
"""
plt.figure(figsize=(8,5))
plt.bar(df["mean"], df["min"], color="green")

plt.title("Reding")
plt.xlabel("mean")
plt.ylabel("min")

plt.show()"""

#df.to_cs("")