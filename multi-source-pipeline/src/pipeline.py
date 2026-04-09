import pandas as pd

# Load Data
def load_data():
    students = pd.read_csv("../data/students.csv")
    behavior = pd.read_csv("../data/behavior.csv")
    return students, behavior


def clean_data(students, behavior):

    behavior["study_hours"] = pd.to_numeric(behavior["study_hours"], errors="coerce")
    behavior["sleep_hours"] = pd.to_numeric(behavior["sleep_hours"], errors="coerce")
    behavior["exam_score"] = pd.to_numeric(behavior["exam_score"], errors="coerce")

    behavior = behavior.dropna()

    return students, behavior

# Merge Data
def merge_data(students, behavior):

    df = pd.merge(students, behavior, on="student_id")

    return df

# Analyze Data
def analyze_data(df):

    print("\nMerged Data:")
    print(df)

    print("\nAverage Score:", df["exam_score"].mean())

    print("\nScore by Age:")
    print(df.groupby("age")["exam_score"].mean())

    print("\nTop sleeper :")
    print(df["sleep_hours"].idxmax())

    print("\nTop Student:")
    print(df.loc[df["exam_score"].idxmax()])

    return df

# Save Results
def save_results(df):
    df.to_csv("../results/report.csv", index=False)

# Main
def main():

    students, behavior = load_data()

    students, behavior = clean_data(students, behavior)

    df = merge_data(students, behavior)

    df = analyze_data(df)

    save_results(df)


if __name__ == "__main__":
    main()