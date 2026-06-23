import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = quote_plus("@*tanushree06*")

engine = create_engine(
    f"postgresql+psycopg2://postgres:{password}@localhost:5432/sales_etl"
)

customer_dim = pd.read_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\output\customer_dim.csv"
)

product_dim = pd.read_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\output\product_dim.csv"
)

fact_sales = pd.read_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\output\fact_sales.csv"
)

customer_dim.to_sql(
    "customer_dim",
    engine,
    if_exists="replace",
    index=False
)

product_dim.to_sql(
    "product_dim",
    engine,
    if_exists="replace",
    index=False
)

fact_sales.to_sql(
    "fact_sales",
    engine,
    if_exists="replace",
    index=False
)

print("Star Schema Loaded Successfully!")