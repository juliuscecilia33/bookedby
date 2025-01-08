import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('./customer_purchase_data.csv')

# Feature Engineering
customer_features = df.groupby('Customer ID').agg({
    'Purchase Amount': 'sum',            # Total Spending
    'Product ID': 'count',               # Purchase Frequency
    'Product Category': pd.Series.nunique  # Unique Product Categories
}).rename(columns={
    'Purchase Amount': 'Total Spending',
    'Product ID': 'Purchase Frequency',
    'Product Category': 'Unique Categories'
})

# Normalize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(customer_features)

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
customer_features['Cluster'] = kmeans.fit_predict(scaled_features)

# Label the clusters based on their characteristics
customer_features['Cluster Label'] = customer_features['Cluster'].map({
    0: "High Spenders",
    1: "Occasional Buyers",
    2: "Bargain Hunters"
})

# Display the cluster summary
print("Clustered Customer Data:")
print(customer_features.head())

# Visualize the clusters (optional)
plt.figure(figsize=(10, 6))
plt.scatter(
    customer_features['Total Spending'], 
    customer_features['Purchase Frequency'], 
    c=customer_features['Cluster'], cmap='viridis'
)
plt.title("Customer Clusters")
plt.xlabel("Total Spending")
plt.ylabel("Purchase Frequency")
plt.colorbar(label="Cluster")
plt.show()
