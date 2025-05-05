import os

# This script manages an inventory system for a store.
INVENTORY_FILE = "inventory.txt"


# This script manages an inventory system.
def add_items():
    try:
        num_items = int(input("How many items do you want to add? "))
        with open(INVENTORY_FILE, "a") as file:
            for _ in range(num_items):
                name = input("Enter item name: ").strip()
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                file.write(f"{name},{price},{quantity}\n")
        print(f"Successfully added {num_items} item(s).")
    except ValueError:
        print(
            "Invalid input. Please enter numeric values for price and "
            "quantity."
        )
    except Exception as e:
        print(f"An error occurred: {e}")


# This function reads the inventory file and displays.
def view_inventory():
    try:
        if not os.path.exists(INVENTORY_FILE):
            print("Inventory file not found.")
            return

        total_value = 0.0
        print(
            (
                f"{'No.':<5} {'Item':<20} {'Price':<10} "
                f"{'Quantity':<10} {'Value':<10}"
            )
        )
        print("-" * 60)

        with open(INVENTORY_FILE, "r") as file:
            for i, line in enumerate(file, 1):
                try:
                    name, price, quantity = line.strip().split(",")
                    price = float(price)
                    quantity = int(quantity)
                    value = price * quantity
                    total_value += value
                    print(
                        (
                            f"{i:<5} {name:<20} {price:<10.2f} "
                            f"{quantity:<10} {value:<10.2f}"
                        )
                    )
                except ValueError:
                    print(f"Skipping malformed line {i}.")

        print("-" * 60)
        print(f"Total inventory value: ${total_value:.2f}")
    except Exception as e:
        print(f"An error occurred while reading the inventory: {e}")


# This function updates the quantity of an item in the inventory.
def update_quantity():
    try:
        if not os.path.exists(INVENTORY_FILE):
            print("Inventory file not found.")
            return

        with open(INVENTORY_FILE, "r") as file:
            items = [line.strip().split(",") for line in file if line.strip()]

        for i, (name, price, quantity) in enumerate(items, 1):
            print(f"{i}. {name} (Price: ${price}, Quantity: {quantity})")

        choice = int(input("Enter the item number to update: "))
        if 1 <= choice <= len(items):
            new_quantity = int(input("Enter new quantity: "))
            items[choice - 1][2] = str(new_quantity)

            with open(INVENTORY_FILE, "w") as file:
                for item in items:
                    file.write(",".join(item) + "\n")
            print("Quantity updated successfully.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")


# This function is the main entry point of the program.
def main():
    while True:
        print("\nInventory Management System")
        print("a. Add new items")
        print("b. View current inventory")
        print("c. Update item quantities")
        print("d. Exit")
        choice = input("Choose an option (a/b/c/d): ").strip().lower()

        if choice == "a":
            add_items()
        elif choice == "b":
            view_inventory()
        elif choice == "c":
            update_quantity()
        elif choice == "d":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a, b, c, or d.")


# This is the entry point of the script.
if __name__ == "__main__":
    main()
