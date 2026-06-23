import pandas as pd

df = pd.read_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\data\Sample - Superstore.csv",
    encoding="latin1"
)

print(df.head())
print()
print(df.columns)