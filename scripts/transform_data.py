import pandas as pd

df = pd.read_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\data\Sample - Superstore.csv",
    encoding="latin1"
)

# Revenue Column
df["Revenue"] = df["Sales"]

# Profit Margin %
df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100

print(df[["Sales", "Profit", "Revenue", "Profit_Margin"]].head())

df.to_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\output\clean_sales.csv",
    index=False
)

print("Clean dataset saved successfully!")