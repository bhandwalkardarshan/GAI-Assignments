from prettytable import PrettyTable

# Sample JSON data
data = [
    {"id": 1, "name": "Item A", "price": 10.99},
    {"id": 2, "name": "Item B", "price": 7.99},
    {"id": 3, "name": "Item C", "price": 12.99},
]

# Create a PrettyTable object and specify column names
table = PrettyTable(["ID", "Name", "Price"])

# Add data rows to the table
for item in data:
    table.add_row([item["id"], item["name"], item["price"]])

# Print the table
print(table)
