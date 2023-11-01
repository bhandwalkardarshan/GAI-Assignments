
# how to add to json file 
# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# # Specify the file path where you want to write the data.
# file_path = "data.json"

# # Write the data to the JSON file.
# with open(file_path, "w") as json_file:
#     json.dump(data, json_file)

import json
import uuid
from prettytable import PrettyTable

# Function to get a unique ID from the console
def get_unique_id():
    return input("Enter a unique ID for the menu item: ")

# Check if a menu item with the same name already exists
def is_menu_item_exists(menu_data, new_item):
    for item in menu_data:
        if item["name"] == new_item["name"]:
            return True
    return False

#  Adding menu to db i.e. menu.json
def add_menu_item(menu_file, new_item):
    try:
        # Read the existing menu data from the JSON file
        with open(menu_file, "r") as file:
            menu_data = json.load(file)

        # Check if the menu item already exists
        if is_menu_item_exists(menu_data, new_item):
            print(f"Item '{new_item['name']}' already exists in the menu.")
            return

        # Prompt the user for a unique ID
        new_item["id"] = get_unique_id()

        # Append the new menu item to the existing menu data
        menu_data.append(new_item)

        # Write the updated data back to the JSON file
        with open(menu_file, "w") as file:
            json.dump(menu_data, file, indent=4)

        print("Menu item added successfully.")
    except Exception as e:
        print("An error occurred while adding the menu item:", str(e))

 # Find a menu item by its name
def find_menu_item_by_name(menu_data, name):
    for item in menu_data:
        if item["name"] == name:
            return item
    return None

# Update an existing menu item's price and description
def update_menu_item(menu_file, item_name, updated_attributes):
    try:
        # Read the existing menu data from the JSON file
        with open(menu_file, "r") as file:
            menu_data = json.load(file)

        # Find the menu item by name
        item_to_update = find_menu_item_by_name(menu_data, item_name)

        if item_to_update:
            # Update the menu item with the provided attributes
            for key, value in updated_attributes.items():
                item_to_update[key] = value

            # Write the updated data back to the JSON file
            with open(menu_file, "w") as file:
                json.dump(menu_data, file, indent=4)

            print(f"Menu item '{item_name}' has been updated.")
        else:
            print(f"Menu item '{item_name}' not found in the menu.")

    except Exception as e:
        print("An error occurred while updating the menu item:", str(e))

# To delete menu
def delete_menu_item_by_name(menu_file, item_name):
    try:
        # Read the existing menu data from the JSON file
        with open(menu_file, "r") as file:
            menu_data = json.load(file)

        # Find the menu item by name
        item_to_delete = find_menu_item_by_name(menu_data, item_name)

        if item_to_delete:
            # Remove the menu item from the list
            menu_data.remove(item_to_delete)

            # Write the updated data back to the JSON file
            with open(menu_file, "w") as file:
                json.dump(menu_data, file, indent=4)

            print(f"Menu item '{item_name}' has been deleted.")
        else:
            print(f"Menu item '{item_name}' not found in the menu.")

    except Exception as e:
        print("An error occurred while deleting the menu item:", str(e))

# to display menu
def display_menu_from_file(menu_file):
    try:
        # Read the menu data from the JSON file
        with open(menu_file, "r") as file:
            menu_data = json.load(file)

        # Create a PrettyTable object with column names
        table = PrettyTable(["Name", "Price", "Availability"])

        # Add menu items to the table
        for item in menu_data:
            table.add_row([item["name"], item["price"], "Available" if item["availability"] else "Not Available"])

        # Set the column alignment to left
        for field in table.field_names:
            table.align[field] = 'l'

        # Print the table
        print(table)

    except Exception as e:
        print("An error occurred while reading and displaying the menu:", str(e))

# to place order
def place_order(orders, menu_file):
    try:
        # Read the menu data from the JSON file
        with open(menu_file, "r") as file:
            menu_data = json.load(file)

        while True:
            display_menu_from_file(menu_file)
            
            # Get the customer's choice
            item_name = input("Enter the name of the item you want to order (or 'q' to quit): ")
            if item_name.lower() == 'q':
                break

            # Find the selected item in the menu
            selected_item = None
            for item in menu_data:
                if item["name"] == item_name:
                    selected_item = item
                    break

            if selected_item:
                # Check if the item is available
                if selected_item["availability"]:
                    # Add the item to the customer's order
                    if "order" not in orders:
                        orders["order"] = []
                    orders["order"].append(selected_item)
                    print(f"{item_name} has been added to your order.")
                else:
                    print(f"{item_name} is not available.")
            else:
                print(f"{item_name} is not found in the menu.")

    except Exception as e:
        print("An error occurred while placing the order:", str(e))


def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add New Menu Item")
        print("2. Update Menu Item")
        print("3. Delete Menu Item")
        print("4. Display Menu")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_menu_item()
        elif choice == "2":
            update_menu_item()
        elif choice == "3":
            delete_menu_item()
        elif choice == "4":
            display_menu_from_file(menu_file_path)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select a valid option.")

def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. Display Menu")
        print("2. Place Order")
        print("3. Delete Item from Order")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu_from_file(menu_file_path)
        elif choice == "2":
            place_order(orders, menu_file_path)
        elif choice == "3":
            delete_order(orders)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

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