from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a PDF canvas object
file_name = "BookedBy_Report.pdf"
c = canvas.Canvas(file_name, pagesize=letter)

# Title
c.setFont("Helvetica-Bold", 18)
c.drawString(100, 750, "Report by Julius Cecilia for BookedBy")

# Insights from Data Analysis Section
c.setFont("Helvetica-Bold", 14)
c.drawString(100, 720, "Insights from Data Analysis")

# Top-Selling Products Table
c.setFont("Helvetica-Bold", 12)
c.drawString(100, 680, "Top-Selling Products")
c.setFont("Helvetica", 10)
c.drawString(100, 660, "Product ID | Sales Count")
c.line(100, 658, 500, 658)

top_selling_products = [
    ('PROD0048', 133), ('PROD0040', 122), ('PROD0031', 121), 
    ('PROD0045', 118), ('PROD0034', 118), ('PROD0003', 115), 
    ('PROD0049', 114), ('PROD0037', 113), ('PROD0041', 109), 
    ('PROD0021', 109)
]
y_position = 640
for product in top_selling_products:
    c.drawString(100, y_position, f"{product[0]} | {product[1]}")
    y_position -= 15

# Top-Selling Categories Table
c.setFont("Helvetica-Bold", 12)
c.drawString(100, y_position - 10, "Top-Selling Categories")
c.setFont("Helvetica", 10)
c.drawString(100, y_position - 30, "Product Category | Sales Count")
c.line(100, y_position - 32, 500, y_position - 32)

top_selling_categories = [
    ('Books', 1536), ('Sports', 916), ('Clothing', 791),
    ('Toys', 702), ('Groceries', 577), ('Electronics', 478)
]
y_position -= 40
for category in top_selling_categories:
    c.drawString(100, y_position, f"{category[0]} | {category[1]}")
    y_position -= 15

# Average Spending Per Customer Table
c.setFont("Helvetica-Bold", 12)
c.drawString(100, y_position - 10, "Average Spending Per Customer")
c.setFont("Helvetica", 10)
c.drawString(100, y_position - 30, "Customer ID | Average Spending")
c.line(100, y_position - 32, 500, y_position - 32)

avg_spending = [
    ('CUST0001', 304.05), ('CUST0002', 259.49), ('CUST0003', 235.82),
    ('CUST0004', 267.77), ('CUST0005', 210.19)
]
y_position -= 40
for spending in avg_spending:
    c.drawString(100, y_position, f"{spending[0]} | {spending[1]}")
    y_position -= 15

# Customer Segments Table
c.setFont("Helvetica-Bold", 12)
c.drawString(100, y_position - 10, "Customer Segments")
c.setFont("Helvetica", 10)
c.drawString(100, y_position - 30, "Customer ID | Total Spending | Purchase Frequency | Unique Categories | Cluster | Cluster Label")
c.line(100, y_position - 32, 500, y_position - 32)

customer_segments = [
    ('CUST0001', 3648.61, 12, 6, 0, 'High Spenders'),
    ('CUST0002', 4670.88, 18, 5, 0, 'High Spenders'),
    ('CUST0003', 2594.02, 11, 3, 1, 'Occasional Buyers'),
    ('CUST0004', 2142.14, 8, 3, 1, 'Occasional Buyers'),
    ('CUST0005', 1681.53, 8, 3, 1, 'Occasional Buyers')
]
y_position -= 50
for segment in customer_segments:
    c.drawString(100, y_position, f"{segment[0]} | {segment[1]} | {segment[2]} | {segment[3]} | {segment[4]} | {segment[5]}")
    y_position -= 15

# Recommended Products for CUST0001
c.setFont("Helvetica-Bold", 12)
c.drawString(100, y_position - 10, "Recommended Products for Customer CUST0001")
c.setFont("Helvetica", 10)
recommended_products = ['PROD0020', 'PROD0003', 'PROD0022', 'PROD0048', 'PROD0034']
y_position -= 30
for product in recommended_products:
    c.drawString(100, y_position, f"- {product}")
    y_position -= 15

# Save the PDF
c.save()
print("PDF report generated successfully!")
