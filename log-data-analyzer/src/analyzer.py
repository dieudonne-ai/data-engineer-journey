import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df["response_time"] = pd.to_numeric(df["response_time"], errors="coerce")
    df = df.dropna()
    return df

def analyze_data(df):
    print("\nTotal Request:", len(df))
    print("\nAverage Response time:" , df["response_time"].mean())
    
    print("\nSlowest Request:")
    print(df.loc[df["response_time"].idxmax()])

    print("\nError Count:")
    print(df[df["status"] == "failed"].shape[0])

    print("\nMost frequent action:")
    print(df["action"].value_counts().idxmax())

    print("\nTotal percentage of failed requests:")
    print((df[df["status"] == "failed"].shape[0] / len(df)) * 100, "%")

    return df

def save_results(df):
    df.to_csv("../results/report.csv", index=False)

def main():
    df = load_data("../data/logs.csv")
    df = clean_data(df)
    df = analyze_data(df)
    save_results(df)

if __name__ == "__main__":
    main()