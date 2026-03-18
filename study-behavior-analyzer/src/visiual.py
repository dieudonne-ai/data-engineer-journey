import matplotlib.pyplot as plt
import pandas as pd

def load_file(file_path):
    df = pd.read_csv(file_path)
    return df

def plot_score_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df["exam_score"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Exam Score Distribution")
    plt.xlabel("Exam Score")
    plt.ylabel("Frequency")
    plt.grid(axis="y", alpha=0.75)
    plt.show()

def plot_study_hours_vs_score(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df["study_hours"], df["exam_score"], color="orange", edgecolor="black")
    plt.title("Study Hours vs Exam Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Exam Score")
    plt.grid()
    plt.show()

def plot_sleep_hours_vs_score(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df["sleep_hours"], df["exam_score"], color="lightgreen", edgecolor="black")
    plt.title("Sleep Hours vs Exam Score")
    plt.xlabel("Sleep Hours")
    plt.ylabel("Exam Score")
    plt.grid()
    plt.show()

def correlation_heatmap(df):
        plt.figure(figsize=(10, 6))
        corr = df.corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()

def main():
    df = load_file("../data/student_behavior.csv")
    plot_score_distribution(df)
    plot_study_hours_vs_score(df)
    plot_sleep_hours_vs_score(df)
    correlation_heatmap(df)

if __name__ == "__main__":
    main()