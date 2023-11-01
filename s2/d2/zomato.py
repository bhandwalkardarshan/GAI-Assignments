import json
from prettytable import PrettyTable

menu_file_path = "menu.json"

# Function to get a unique ID from the console
def get_unique_id():
    return input("Enter a unique ID for the menu item: ")

# Function to read menu data from the file
def read_menu_data():
    try:
        with open(menu_file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to write menu data to the file
def write_menu_data(menu_data):
    with open(menu_file_path, "w") as file:
        json.dump(menu_data, file, indent=4)

# Check if a menu item with the same name already exists
def is_menu_item_exists(menu_data, new_item):
    for item in menu_data:
        if item["name"] == new_item["name"]:
            return True
    return False

# Function to add a new menu item
def add_new_menu_item():
    try:
        menu_data = read_menu_data()
        new_item = {"name": input("Enter the item name: "),
                    "price": float(input("Enter the price: ")),
                    "availability": input("Is it available? (yes or no): ").lower() == "yes"}
        # Check if the menu item already exists
        if is_menu_item_exists(menu_data, new_item):
            print(f"Item '{new_item['name']}' already exists in the menu.")
            return

        # Prompt the user for a unique ID
        new_item["id"] = get_unique_id()
        menu_data.append(new_item)
        write_menu_data(menu_data)
        print("Menu item added successfully.")
    except Exception as e:
        print("An error occurred while adding the menu item:", str(e))

# Function to display menu
def display_menu():
    try:
        menu_data = read_menu_data()
        if not menu_data:
            print("Menu is empty.")
            return
        table = PrettyTable(["Name", "Price", "Availability"])
        for item in menu_data:
            table.add_row([item["name"], item["price"], "Available" if item["availability"] else "Not Available"])
        for field in table.field_names:
            table.align[field] = 'l'
        print(table)
    except Exception as e:
        print("An error occurred while reading and displaying the menu:", str(e))

# ...

# Function to delete an item from the customer's order
def delete_order(orders):
    if "order" not in orders:
        print("Your order is empty.")
    else:
        print("Your Order:")
        for i, item in enumerate(orders["order"]):
            print(f"{i + 1}. {item['name']} - ${item['price']:.2f}")

        try:
            item_number = int(input("Enter the number of the item you want to remove: ")) - 1

            if 0 <= item_number < len(orders["order"]):
                removed_item = orders["order"].pop(item_number)
                print(f"{removed_item['name']} has been removed from your order.")
            else:
                print("Invalid item number. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to place an order
def place_order(orders):
    while True:
        menu_data = read_menu_data()
        display_menu()
        item_name = input("Enter the name of the item you want to order (or 'q' to quit): ")
        if item_name.lower() == 'q':
            break

        selected_item = None
        for item in menu_data:
            if item["name"] == item_name:
                selected_item = item
                break

        if selected_item:
            if selected_item["availability"]:
                if "order" not in orders:
                    orders["order"] = []
                orders["order"].append(selected_item)
                print(f"{item_name} has been added to your order.")
            else:
                print(f"{item_name} is not available.")
        else:
            print(f"{item_name} is not found in the menu.")

# Main function for the admin menu
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add New Menu Item")
        print("2. Display Menu")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_new_menu_item()
        elif choice == "2":
            display_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Main function for the customer menu
def customer_menu():
    orders = {"order": []}
    while True:
        print("\nCustomer Menu:")
        print("1. Display Menu")
        print("2. Place Order")
        print("3. Delete Item from Order")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_menu()
        elif choice == "2":
            place_order(orders)
        elif choice == "3":
            delete_order(orders)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Main function
def main():
    print("Welcome to Zomato Chronicles: The Great Food Fiasco!")
    # Ask for the user's role (admin or customer)
    user_role = input("Please enter your role (admin or customer): ").lower()
    if user_role == "admin":
        admin_menu()
    elif user_role == "customer":
        customer_menu()
    else:
        print("Invalid role. Please enter 'admin' or 'customer'.")

if __name__ == "__main__":
    main()
