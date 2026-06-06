import pandas as pd
from faker import Faker
import random

fake = Faker('en_IN')

regions = ['North', 'South', 'East', 'West']

categories = {
    'Electronics': ['Mobile Phone', 'Laptop', 'Tablet', 'Headphones'],
    'Clothing': ['T-Shirt', 'Jeans', 'Saree', 'Kurta'],
    'Food': ['Rice', 'Oil', 'Sugar', 'Coffee'],
    'Furniture': ['Chair', 'Table', 'Sofa', 'Bookshelf']
}

segments = ['Retail', 'Wholesale', 'Online']

price_map = {
    'Mobile Phone': 15000, 'Laptop': 45000, 'Tablet': 20000, 'Headphones': 2000,
    'T-Shirt': 500, 'Jeans': 1200, 'Saree': 3000, 'Kurta': 800,
    'Rice': 100, 'Oil': 200, 'Sugar': 50, 'Coffee': 300,
    'Chair': 3000, 'Table': 5000, 'Sofa': 15000, 'Bookshelf': 4000
}

data = []

for i in range(10000):
    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])
    quantity = random.randint(1, 10)
    unit_price = price_map[product]
    total_sales = quantity * unit_price

    row = {
        'Date': fake.date_between(start_date='-2y', end_date='today'),
        'Region': random.choice(regions),
        'Category': category,
        'Product': product,
        'Quantity': quantity,
        'Unit_Price': unit_price,
        'Total_Sales': total_sales,
        'Customer_Segment': random.choice(segments)
    }
    data.append(row)

df = pd.DataFrame(data)
df.to_csv('retail_sales_data.csv', index=False)
print("Done! 10,000 rows generated.")