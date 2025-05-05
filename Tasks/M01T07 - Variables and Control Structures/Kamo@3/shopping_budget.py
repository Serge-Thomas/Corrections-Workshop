
# Main program
def main():
    # Ask the user to enter their shopping budget
    budget = float(input("Enter your shopping budget: R"))
    shopping_list = {}  # Dictionary to store items and their prices
    total_spent = 0.0   # Total amount spent

    while True:
        # Prompt user to add items or checkout
        item = input("Enter an item (or type 'checkout' to finish): ")
        
        if item.lower() == "checkout":
            # User is done shopping
            break
        
        # Ask user to enter the item price
        price = float(input(f"Enter the price for {item}: R"))
        
        # Check if the new purchase exceeds the budget
        if total_spent + price > budget:
            print("You have exceeded your budget!")
            remove_item = input("Would you like to remove an item? (yes/no): ").lower()
            if remove_item == "yes":
                item_to_remove = input("Enter the name of the item to remove: ")
                if item_to_remove in shopping_list:
                    total_spent -= shopping_list[item_to_remove]  # Subtract its price from total spent
                    del shopping_list[item_to_remove]  # Remove item from shopping list
                    print(f"{item_to_remove} has been removed from your shopping list.")
                else:
                    print(f"{item_to_remove} is no longer in your shopping list.")
                
        else:
            # Add item to the shopping list
            shopping_list[item] = price
            total_spent += price
            remaining_budget = budget - total_spent
            print(f"Item added: {item}, Price: R{price:.2f}")
            print(f"Remaining budget: R{remaining_budget:.2f}")

# Display final shopping list and budget status
    display_final_list(shopping_list, total_spent, budget)


# Function to display the final shopping list and budget status
def display_final_list(shopping_list, total_spent, budget):
    print("\nFinal Shopping List:")
    for item, price in shopping_list.items():
        print(f"{item}: R{price:.2f}")
    remaining_budget = budget - total_spent
    print(f"\nTotal spent: R{total_spent:.2f}")
    print(f"Remaining budget: R{remaining_budget:.2f}")

# Running the main function


if __name__ == "__main__":
    main()
