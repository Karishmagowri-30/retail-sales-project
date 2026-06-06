import pandas as pd
import pymysql
from sqlalchemy import create_engine

# Connect to MySQL
engine = create_engine('mysql+pymysql://root:Karishma%403011@localhost/retail_sales')
# Read data from MySQL into Pandas
df = pd.read_sql('SELECT * FROM sales', engine)

print(df.shape)
print(df.head())
# 1. Check for missing values
print("Missing values:")
print(df.isnull().sum())

# 2. Sales by Region
region_sales = df.groupby('Region')['Total_Sales'].sum().reset_index()
region_sales = region_sales.sort_values('Total_Sales', ascending=False)
print("\nSales by Region:")
print(region_sales)

# 3. Sales by Category
category_sales = df.groupby('Category')['Total_Sales'].sum().reset_index()
category_sales = category_sales.sort_values('Total_Sales', ascending=False)
print("\nSales by Category:")
print(category_sales)

# 4. Top 5 Products
top_products = df.groupby('Product')['Total_Sales'].sum().reset_index()
top_products = top_products.sort_values('Total_Sales', ascending=False).head(5)
print("\nTop 5 Products:")
print(top_products)