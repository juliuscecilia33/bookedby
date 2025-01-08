import pandas as pd

# Load the dataset
df = pd.read_csv('/mnt/data/customer_purchase_data.csv')

# Identify top-selling products
top_products = df['Product ID'].value_counts().head(10)

# Identify top-selling categories
top_categories = df['Product Category'].value_counts()

# Calculate average spending per customer
average_spending_per_customer = df.groupby('Customer ID')['Purchase Amount'].mean()

# Display the results
print("Top-Selling Products (Product ID: Sales Count):")
print(top_products)

print("\nTop-Selling Categories (Category: Sales Count):")
print(top_categories)

print("\nAverage Spending Per Customer (Customer ID: Average Spending):")
print(average_spending_per_customer.head())  # Displaying the first 5 customers for brevity
