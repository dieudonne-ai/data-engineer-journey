import pandas as pd

df = pd.read_csv("data/students.csv")

"""def get_score(score):
    try:
        score = int(score)
    except (ValueError, TypeError):
        return "N/A"

    if pd.isna(score):
        return "N/A"
    elif score >= 20:
        return "A"
    elif score >= 16:
        return "B"
    elif score >= 12:
        return "C"
    elif score >= 8:
        return "D"
    else:
        return "F"
"""

#df["score"] = df["Score"].apply(get_score)
df.to_csv("clean_data/students_with_grades.csv", index=False)

"""print(df.head())
print(df.info())
print(df)"""

print("A clean copy of your file is already saved in Clean_data folder")
