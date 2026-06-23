import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = quote_plus("@*tanushree06*")   # apna actual password

engine = create_engine(
    f"postgresql+psycopg2://postgres:{password}@localhost:5432/sales_etl"
)

df = pd.read_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\output\clean_sales.csv"
)

df.to_sql(
    "sales_data",
    engine,
    if_exists="replace",
    index=False
)

print("Data Loaded Successfully!")