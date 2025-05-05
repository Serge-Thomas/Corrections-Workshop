import os


def display_menu():
    print("\n--- Inventory Manager ---")
    print("a. Add new items to inventory")
    print("b. View current inventory")
    print("c. Update item quantities")
    print("d. Exit the program")


def add_items():
    try:
        count = int(input("How many items do you want to add? "))
        with open("inventory.txt", "a") as file:
            for _ in range(count):
                name = input("Enter item name: ").strip()
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                file.write(f"{name},{price},{quantity}\n")
        print("Items added successfully.")
    except ValueError:
        print("Invalid input. Enter value.")
    except Exception as e:
        print(f"An error occurred: {e}")


def view_inventory():
    print("\n--- Current Inventory ---")
    if not os.path.exists("inventory.txt"):
        print("No inventory file found.")
        return
    try:
        total_value = 0
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("Inventory is empty.")
                return
            print(f"{'No.':<4} {'Item':<20} {'Price':<10} {'Quantity':<10} {'Total':<10}")
            for i, line in enumerate(lines, 1):
                name, price, quantity = line.strip().split(',')
                price = float(price)
                quantity = int(quantity)
                item_total = price * quantity
                total_value += item_total
                print(f"{i:<4} {name:<20} {price:<10.2f} {quantity:<10} {item_total:<10.2f}")
            print(f"\nTotal inventory value: ${total_value:.2f}")
    except Exception as e:
        print(f"An error occurred while reading the inventory: {e}")


def update_quantity():
    if not os.path.exists("inventory.txt"):
        print("No inventory file found.")
        return
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
        if not lines:
            print("Inventory is empty.")
            return

        view_inventory()

        index = int(input("Enter the item number to update: ")) - 1
        if index < 0 or index >= len(lines):
            print("Invalid item number.")
            return

        name, price, _ = lines[index].strip().split(',')
        new_quantity = int(input(f"Enter new quantity for {name}: "))
        lines[index] = f"{name},{price},{new_quantity}\n"

        with open("inventory.txt", "w") as file:
            file.writelines(lines)

        print("Quantity updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred while updating inventory: {e}")


def main():
    while True:
        display_menu()
        choice = input("Select an option (a/b/c/d): ").lower()
        if choice == 'a':
            add_items()
        elif choice == 'b':
            view_inventory()
        elif choice == 'c':
            update_quantity()
        elif choice == 'd':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
