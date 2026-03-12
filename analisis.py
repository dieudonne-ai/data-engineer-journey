import pandas as pd

df = pd.read_csv("data/students.csv")


df ["score"] = pd.to_numeric(df["score"], errors="coerce")

def get_grade(score):
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
df["grade"] = df["score"].apply(get_grade)

passed = df[df["score"] >= 10]
failed = df[df["score"] < 10]
top_students = df[df["score"] == df["score"].max()]
avg = df["score"].mean()


print("Average score:", avg)
print("Highest score:", df ["score"].max())
print("Lowest score:", df ["score"].min())

print("Passed students:", passed, " ")
print("Failed students:", failed, "")
print("Top students is :", top_students)
print("Grade distribution:")
print(df["grade"].value_counts())


"""
to day i have done the following things:
1. I have read the students.csv file using pandas.
2. I have converted the score column to numeric, handling any non-numeric values as NaN.
3. I have defined a function get_grade to assign letter grades based on the score.
4. I have applied the get_grade function to create a new grade column in the DataFrame.
5. I have filtered the DataFrame to get passed students (score >= 10) and
    failed students (score < 10).
6. I have calculated the average score, highest score, and lowest score.
7. I have printed the average score, highest score, lowest score, passed students, failed
    students, top students, and the grade distribution.
"""
