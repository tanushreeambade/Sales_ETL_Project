import pandas as pd

df = pd.read_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\data\Sample - Superstore.csv",
    encoding="latin1"
)

print("DATASET SHAPE")
print(df.shape)

print("\nCOLUMN INFO")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATES")
print(df.duplicated().sum())