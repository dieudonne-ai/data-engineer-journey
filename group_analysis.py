import pandas as pd

df = pd.read_csv("data/students.csv")
df["score"] = pd.to_numeric(df["score"], errors="coerce")

def get_grade(score):
    if pd.isna(score):
        return "N/A"
    elif score >= 18:
        return "A"
    elif score >= 16:
        return "B"
    elif score >= 14:
        return "C"
    elif score >= 12:
        return "D"
    else:
        return "F"

df["grade"] = df["score"].apply(get_grade)

#Grade_summary = df.groupby("grade")["score"].mean()
#grade_count = df.groupby("grade")["name"].count()

summary = df.groupby("grade")["score"].agg(["mean", "count", "min", "max"])


print(Grade_summary)
print(summary)