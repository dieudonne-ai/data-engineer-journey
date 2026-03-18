import pandas as pd

# Load Data

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    df = df.dropna()

    df["study_hours"] = pd.to_numeric(df["study_hours"], errors="coerce")
    df["sleep_hours"] = pd.to_numeric(df["sleep_hours"], errors="coerce")
    df["social_media_hours"] = pd.to_numeric(df["social_media_hours"], errors="coerce")
    df["exam_score"] = pd.to_numeric(df["exam_score"], errors="coerce")

    return df

# Analyze Data

def analyze_data(df):

    print("\nAverage Score:", df["exam_score"].mean())

    print("\nTop Student:")
    print(df.loc[df["exam_score"].idxmax()])

    print("\nCorrelation Matrix:")
    print(df.corr())

    return df.corr()

# Save Results

def save_results(corr):
    corr.to_csv("../results/report.csv")

def main():

    df = load_data("../data/student_behavior.csv")

    df = clean_data(df)

    corr = analyze_data(df)

    save_results(corr)


if __name__ == "__main__":
    main()