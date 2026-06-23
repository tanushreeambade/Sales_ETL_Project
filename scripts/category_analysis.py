import pandas as pd

df = pd.read_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\data\Sample - Superstore.csv",
    encoding="latin1"
)

category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("CATEGORY REVENUE")
print(category_sales)