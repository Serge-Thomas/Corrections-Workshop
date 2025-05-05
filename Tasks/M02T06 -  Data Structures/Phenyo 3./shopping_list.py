# This code creates a shopping list.
# The user can add items to the list until they type 'done'
def main():
    shopping_list = []

    while True:
        item = input(
            "Enter item to add to shopping list (or 'done' to finish): "
        ).strip()
        if item.lower() == "done":
            break
        shopping_list.append(item)

    shopping_list.sort()
    print("Your shopping list:", shopping_list)


# This code will call the main function when the script runs.
if __name__ == "__main__":
    main()
