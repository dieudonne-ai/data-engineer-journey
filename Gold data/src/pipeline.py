import pandas as pd
import numpy as np

def load_data(path):
    df = pd.read_csv(path)
    return df


# 1. Charger le fichier
df = load_data("../data/Gold_Data.csv")

# 2. Nettoyer les colonnes prix (Price, Open, High, Low)


# 3. Nettoyer le volume (Vol.) → convertir "0.65K" en 650
def clean_volume(x):
    if pd.isna(x) or x == '':
        return np.nan
    x = str(x).strip().upper()
    if 'K' in x:
        return float(x.replace('K', '')) * 1000
    return float(x)



# 4. Nettoyer le changement en % 
# 5. Convertir la date


# Afficher le résultat


def clean_data(df):
    for col in ['Price', 'Open', 'High', 'Low']:
        df[col] = df[col].str.replace(',', '', regex=False).astype(float)
        df['Vol.'] = df['Vol.'].apply(clean_volume)
        df['Change %'] = df['Change %'].str.replace('%', '', regex=False).astype(float)
        df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
    return df

def analyze_data(df):
    print(df.shape)
    print(df.info())

    print(df.head())
    print("\nTypes de données après nettoyage :")
    print(df.dtypes)
    return df.describe()


def main():
    df = load_data("../data/Gold_Data.csv")
    df = clean_data(df)
    summary = analyze_data(df)
    print(summary)


if __name__ == "__main__":
    main()    