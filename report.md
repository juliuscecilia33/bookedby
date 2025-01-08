# Report by Julius Cecilia for BookedBy

## Insights from Data Analysis

### Top-Selling Products

| Product ID | Sales Count |
| ---------- | ----------- |
| PROD0048   | 133         |
| PROD0040   | 122         |
| PROD0031   | 121         |
| PROD0045   | 118         |
| PROD0034   | 118         |
| PROD0003   | 115         |
| PROD0049   | 114         |
| PROD0037   | 113         |
| PROD0041   | 109         |
| PROD0021   | 109         |

### Top-Selling Categories

| Product Category | Sales Count |
| ---------------- | ----------- |
| Books            | 1536        |
| Sports           | 916         |
| Clothing         | 791         |
| Toys             | 702         |
| Groceries        | 577         |
| Electronics      | 478         |

### Average Spending Per Customer

| Customer ID | Average Spending |
| ----------- | ---------------- |
| CUST0001    | 304.05           |
| CUST0002    | 259.49           |
| CUST0003    | 235.82           |
| CUST0004    | 267.77           |
| CUST0005    | 210.19           |

## Customer Segments

### Clustered Customer Data

| Customer ID | Total Spending | Purchase Frequency | Unique Categories | Cluster | Cluster Label     |
| ----------- | -------------- | ------------------ | ----------------- | ------- | ----------------- |
| CUST0001    | 3648.61        | 12                 | 6                 | 0       | High Spenders     |
| CUST0002    | 4670.88        | 18                 | 5                 | 0       | High Spenders     |
| CUST0003    | 2594.02        | 11                 | 3                 | 1       | Occasional Buyers |
| CUST0004    | 2142.14        | 8                  | 3                 | 1       | Occasional Buyers |
| CUST0005    | 1681.53        | 8                  | 3                 | 1       | Occasional Buyers |

## Example Recommendationsfor a sepcific customer (CUST0001)

````Recommended Products for Customer CUST0001:
['PROD0020', 'PROD0003', 'PROD0022', 'PROD0048', 'PROD0034']```
````

### Customer Data

| Customer ID | Total Spending | Purchase Frequency | Unique Categories | Cluster |
| ----------- | -------------- | ------------------ | ----------------- | ------- |
| CUST0001    | 3648.61        | 12                 | 6                 | 0       |
| CUST0002    | 4670.88        | 18                 | 5                 | 0       |
| CUST0003    | 2594.02        | 11                 | 3                 | 1       |
| CUST0004    | 2142.14        | 8                  | 3                 | 1       |
| CUST0005    | 1681.53        | 8                  | 3                 | 1       |
