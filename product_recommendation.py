import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Load the dataset
df = pd.read_csv('./customer_purchase_data.csv')

# Create a user-item interaction matrix
interaction_matrix = df.pivot_table(
    index='Customer ID', columns='Product ID', values='Purchase Amount', fill_value=0
)

# Convert to sparse matrix for efficiency
sparse_matrix = csr_matrix(interaction_matrix)

# Calculate cosine similarity between products
product_similarity = cosine_similarity(sparse_matrix.T)

# Create a DataFrame for product similarity
product_similarity_df = pd.DataFrame(
    product_similarity, index=interaction_matrix.columns, columns=interaction_matrix.columns
)

# Recommend products for a customer
def recommend_products(customer_id, interaction_matrix, product_similarity_df, n_recommendations=5):
    # Get the products the customer has interacted with
    purchased_products = interaction_matrix.loc[customer_id]
    purchased_products = purchased_products[purchased_products > 0].index.tolist()
    
    # Compute a weighted score for each product based on similarity to purchased products
    scores = product_similarity_df[purchased_products].sum(axis=1).sort_values(ascending=False)
    
    # Remove products the customer already purchased
    recommended_products = scores.drop(labels=purchased_products).head(n_recommendations)
    
    return recommended_products.index.tolist()

# Example: Get recommendations for a customer
customer_id = interaction_matrix.index[0]  # First customer as an example
recommended_products = recommend_products(customer_id, interaction_matrix, product_similarity_df)

print(f"Recommended Products for Customer {customer_id}:")
print(recommended_products)
