# analytics/run_analytics.py
import os
import pandas as pd
import matplotlib.pyplot as plt
import pymysql
from sqlalchemy import create_engine

# ------------------------------
# Database connection
# ------------------------------
DB_USER = "root"
DB_PASSWORD = "zackTimmy678#"
DB_HOST = "127.0.0.1"
DB_NAME = "mock_amazon"

# Using SQLAlchemy for easy pandas integration
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

# ------------------------------
# Create output folder
# ------------------------------
OUTPUT_DIR = "analytics/outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------
# Fetch tables
# ------------------------------
users = pd.read_sql("SELECT * FROM users", engine)
products = pd.read_sql("SELECT * FROM products", engine)
orders = pd.read_sql("SELECT * FROM orders", engine)
order_items = pd.read_sql("SELECT * FROM order_items", engine)

# ------------------------------
# Analytics functions
# ------------------------------
def total_sales_per_product(order_items, products):
    merged = pd.merge(order_items, products, left_on="product_id", right_on="id", suffixes=('_order', '_product'))
    
    # Determine correct price column
    if "price_product" in merged.columns:
        price_col = "price_product"
    elif "price_y" in merged.columns:
        price_col = "price_y"
    else:
        price_col = "price"  # fallback

    merged["revenue"] = merged["quantity"] * merged[price_col]
    sales = merged.groupby("name")[["quantity", "revenue"]].sum().reset_index()
    return sales

def sales_per_user(order_items, users):
    merged = pd.merge(order_items, orders, left_on="order_id", right_on="id", suffixes=('_item', '_order'))
    merged = pd.merge(merged, users, left_on="user_id", right_on="id", suffixes=('', '_user'))
    merged["total_spent"] = merged["quantity"] * merged["price"]
    sales = merged.groupby("name")[["total_spent"]].sum().reset_index()
    return sales

def plot_bar_chart(df, x_col, y_col, title, filename):
    plt.figure(figsize=(10,6))
    plt.bar(df[x_col], df[y_col], color="skyblue")
    plt.xticks(rotation=45, ha="right")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, filename))
    plt.close()

# ------------------------------
# Main
# ------------------------------
def main():
    print("CSV exports saved to:", os.path.abspath(OUTPUT_DIR))
    
    # Total sales per product
    sales_prod = total_sales_per_product(order_items, products)
    sales_prod.to_csv(os.path.join(OUTPUT_DIR, "sales_per_product.csv"), index=False)
    plot_bar_chart(sales_prod, "name", "revenue", "Revenue per Product", "sales_per_product.png")
    
    # Also create an explicit chart with plt.show
    plt.figure(figsize=(10,6))
    plt.bar(sales_prod['name'], sales_prod['revenue'], color='skyblue')
    plt.title("Total Revenue per Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "total_revenue_per_product.png"))
    plt.show()  # optional: show chart locally

    # Sales per user
    sales_user = sales_per_user(order_items, users)
    sales_user.to_csv(os.path.join(OUTPUT_DIR, "sales_per_user.csv"), index=False)
    plot_bar_chart(sales_user, "name", "total_spent", "Total Spent per User", "sales_per_user.png")
    
    print("Analytics completed!")

if __name__ == "__main__":
    main()
