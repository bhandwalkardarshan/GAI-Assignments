
# to add snack
def add_snack(snack_inventory):
    snack_id = input("Enter the snack ID: ")
    snack_name = input("Enter the snack name: ")
    snack_price = input("Enter the snack price in Rs.: ")
    snack_available = input("Is the snack available (yes/no): ").lower()

    if snack_available == "yes":
        available = True
    else :
        available = False

    snack_inventory[snack_id] = {
        "name": snack_name,
        "price": snack_price,
        "availability": available
    }
    print(f"Snack '{snack_name}' added to the inventory")

# to delete snack
def remove_snack(snack_inventory):
    snack_id = input("Enter the snack ID you want to remove: ")
    if snack_id in snack_inventory:
        del snack_inventory[snack_id]
        print("The specified snack is deleted from the inventory.")
    else:
        print("The specified snack is not present in the inventory.")

# to update snack
def update_snack_availability(snack_inventory):
    snack_id = input("Enter the snack ID you to update availabilty: ")
    if snack_id in snack_inventory:
        snack_available = input("Is snack available (yes/no): ")
        snack_inventory[snack_id]["availability"] = (snack_available == "yes")
        print("The specified snack availability is updated.")
    else:
        print("The specified snack is not present in the inventory.")

# to sell snack
def sell_snack(snack_inventory):
    snack_id = input("Enter the snack ID to be sold: ")

    if snack_id in snack_inventory:
        if snack_inventory[snack_id]["availability"]:
            snack_inventory[snack_id]["availability"] = False
            print("The specified snack has been sold and removed from the inventory.")
        else:
            print("The specified snack is already sold or unavailable.")
    else:
        print("The specified snack is not present in the inventory.")

# to display available snacks
def display_snack_inventory(snack_inventory):
    if len(snack_inventory) > 0:
        print('Snacks: ')
        for id, snack_details in snack_inventory.items():
            print(f'ID: {id}, Name: {snack_details["name"]}, Price: {snack_details["price"]}, Availablity: {snack_details["availability"]}')
    else:
        print('Snacks are not available ')

# main function
def main():
    # define the snack inventory dictionary
    snack_inventory = {}
    while True:
        print("\nChoose option for operation: ")
        print("1 - Add a new snack to the inventory")
        print("2 - Remove an existing snack from the inventory")
        print("3 - Update the availability of a specific snack")
        print("4 - Sell a particular snack")
        print("5 - Display all available snacks")
        print("6 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_snack(snack_inventory)
            display_snack_inventory(snack_inventory)
        elif choice == "2":
            remove_snack(snack_inventory)
            display_snack_inventory(snack_inventory)
        elif choice == "3":
            update_snack_availability(snack_inventory)
            display_snack_inventory(snack_inventory)
        elif choice == "4":
            sell_snack(snack_inventory)
            display_snack_inventory(snack_inventory)
        elif choice == "5":
            display_snack_inventory(snack_inventory)
        elif choice == "6":
            print("Exiting the app")
            break
        else:
            print("Invalid Option! Please enter again.")


if __name__ == "__main__":
        main()