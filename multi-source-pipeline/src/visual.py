import matplotlib.pyplot as plt
import pandas as pd

def read_file(path):
    df = pd.read_csv(path)
    return df


def study_Score(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df["study_hours"], df["exam_score"], color="orange", edgecolor="black")
    plt.title("Score Distribution")
    plt.xlabel("Study Hours")
    plt.ylabel("Score")
    plt.grid(axis="y", alpha=0.75)
    plt.show()


def main():
    df = read_file("../results/report.csv")
    study_Score(df)


if __name__ == "__main__":
    main()        