"""
First data pipeline for machine learning model.

in this file we will create a data pipeline to load and preprocess the data for our machine learning model. We will use the pandas library to read the data from a CSV file, and then we will perform some basic preprocessing steps such as handling missing values, encoding categorical variables, and scaling numerical features. 
Finally, we will split the data into training and testing sets to prepare it for model training and evaluation.
"""

import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df = df.dropna()
    df = df[(df["score"] >= 0) & (df["score"] <= 20)]
    return df

def grade(df):
    def get_grade(score):
        if score >= 18:
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
    return df

def analyze_data(df):
    summary = df.groupby("grade")["score"].describe()
    print(summary)
    return summary

def detect_top_students(df):
    df = df.loc[df["grade"] == "A"]
    print("Top students:")
    print(df[["name", "score"]])
    return df

def save_results(summary):
    summary.to_csv("clean_data/grade_summary.csv")

def main():
    df = load_data("data/students.csv")
    df = clean_data(df)
    df = grade(df)
    df = detect_top_students(df)
    summary = analyze_data(df)
    save_results(summary)

if __name__ == "__main__":
    main()
