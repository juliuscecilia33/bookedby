from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load the dataset
df = pd.read_csv('./customer_purchase_data.csv')

# Feature Engineering (using the same features as before)
customer_features = df.groupby('Customer ID').agg({
    'Purchase Amount': 'sum',
    'Product ID': 'count',
    'Product Category': pd.Series.nunique
}).rename(columns={
    'Purchase Amount': 'Total Spending',
    'Product ID': 'Purchase Frequency',
    'Product Category': 'Unique Categories'
})

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(customer_features)

# Apply KMeans Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
customer_features['Cluster'] = kmeans.fit_predict(scaled_features)

# Display the results
print(customer_features.head())
