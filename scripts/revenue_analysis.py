import pandas as pd

df = pd.read_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\data\Sample - Superstore.csv",
    encoding="latin1"
)

state_revenue = (
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("TOP 10 STATES BY REVENUE")
print(state_revenue)