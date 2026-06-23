import pandas as pd

df = pd.read_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\output\clean_sales.csv"
)

# CUSTOMER DIMENSION
customer_dim = df[
    [
        "Customer ID",
        "Customer Name",
        "Segment",
        "City",
        "State",
        "Region"
    ]
].drop_duplicates(subset=["Customer ID"])
# PRODUCT DIMENSION

product_dim = df[
    [
        "Product ID",
        "Product Name",
        "Category",
        "Sub-Category"
    ]
].drop_duplicates(subset=["Product ID"])

# FACT SALES
fact_sales = df[
    [
        "Order ID",
        "Customer ID",
        "Product ID",
        "Sales",
        "Quantity",
        "Discount",
        "Profit"
    ]
]

# SAVE FILES
customer_dim.to_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\output\customer_dim.csv",
    index=False
)

product_dim.to_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\output\product_dim.csv",
    index=False
)

fact_sales.to_csv(
    r"C:\Users\Admin\OneDrive\Desktop\Sales_ETL_Project\output\fact_sales.csv",
    index=False
)

print("Star Schema Files Created Successfully!")

print("\nCustomer Rows:", len(customer_dim))
print("Product Rows:", len(product_dim))
print("Fact Rows:", len(fact_sales))