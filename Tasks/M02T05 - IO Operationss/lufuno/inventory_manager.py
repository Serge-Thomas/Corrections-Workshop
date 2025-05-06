FILENAME = "inventory.txt"


def show_menu():
    print("\n----- Inventory Manager -----")
    print("a. Add new items to inventory")
    print("b. View current inventory")
    print("c. Update item quantities")
    print("d. Exit the program")


def add_items():
    try:
        count = int(input("How many items do you want to add? "))

        # Open the file in append mode so we don't delete existing data
        with open(FILENAME, "a") as file:
            for i in range(count):
                print(f"\nAdding item {i + 1}")
                name = input("Item name: ")
                price = float(input("Item price: "))
                quantity = int(input("Item quantity: "))

                # Save item as a line in the file
                file.write(f"{name},{price},{quantity}\n")

        print("Item(s) added successfully!")

    except ValueError:
        print("Please enter valid numbers for price and quantity.")


def view_inventory():
    try:
        # Open the file in read mode
        with open(FILENAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("Inventory is empty.")
            return

        print("\n--- Current Inventory ---")
        print("{:<5} {:<20} {:<10} {:<10}".format("No.", "Item", "Price",
                                                  "Quantity"))

        total = 0

        for i, line in enumerate(lines, start=1):
            parts = line.strip().split(",")

            if len(parts) == 3:
                name = parts[0]
                price = float(parts[1])
                quantity = int(parts[2])
                value = price * quantity
                total += value

                print("{:<5} {:<20} {:<10.2f} {:<10}".format(i, name, price,
                                                             quantity))

        print(f"\nTotal inventory value: R{total:.2f}")

    except FileNotFoundError:
        print("No inventory found yet. Add items first.")
    except ValueError:
        print("There was an error reading the data. Please check the file.")
    except Exception as e:
        print(f"Something went wrong: {e}")


def update_quantity():
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("Inventory is empty.")
            return

        print("\n--- Update Quantities ---")
        for i, line in enumerate(lines, start=1):
            parts = line.strip().split(",")
            if len(parts) == 3:
                name, price, quantity = parts
                print(f"{i}. {name} - Price: R{price}, Quantity: {quantity}")

        item_number = int(input("Enter the item number to update: "))

        if 1 <= item_number <= len(lines):
            new_quantity = int(input("Enter the new quantity: "))
            parts = lines[item_number - 1].strip().split(",")
            name = parts[0]
            price = parts[1]
            lines[item_number - 1] = f"{name},{price},{new_quantity}\n"

            # Save the updated list back to the file
            with open(FILENAME, "w") as file:
                file.writelines(lines)

            print("Quantity updated successfully!")
        else:
            print("Invalid item number.")

    except FileNotFoundError:
        print("No inventory found yet.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"Something went wrong: {e}")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (a/b/c/d): ").lower()

        if choice == "a":
            add_items()
        elif choice == "b":
            view_inventory()
        elif choice == "c":
            update_quantity()
        elif choice == "d":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option.")


# Run the program
if __name__ == "__main__":
    main()
