import pandas as pd

def load_file(file_path):
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the DataFrame by handling missing values and duplicates."""
    df = df.drop_duplicates()
    df = df.fillna(method='ffill')
    df["price"] = pd.to_numeric(df["price"], errors='coerce')
    df["quantity"] = pd.to_numeric(df["quantity"], errors='coerce')
    df = df.dropna()
    return df    

def transform_data(df):
    """Transform the DataFrame by adding a total sales column."""
    df["revenue"] = df["price"] * df["quantity"]
    return df    

def analyze_data(df):
    print("Total Sales:", df["revenue"].sum())
    print("Average Sales:", df["revenue"].mean())
    print("\nRevenue by Product:")
    print(df.groupby("product")["revenue"].sum())
    print("\nBest Selling Products:")
    print(df.groupby("product")["quantity"].sum().idxmax())
    print("\nSales per day:")
    print(df.groupby("date")["revenue"].sum())
    return df.groupby("date")["revenue"].sum()

def save_results(result):

    """Save the DataFrame to a new CSV file."""
    result.to_csv("../results/sales_summary.csv", index=True)

def main():
    file_path = "../data/sales.csv"
    df = load_file(file_path)
    df = clean_data(df)
    df = transform_data(df)
    result = analyze_data(df)
    save_results(result)

if __name__ == "__main__":
    main()    



    """This pipeline is designed especially for"""
