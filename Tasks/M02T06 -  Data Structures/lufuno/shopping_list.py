def main():
    shopping_list = []

    while True:
        item = input("Enter item to add to shopping list (or 'done' to finish)\
: ").strip()

        if item.lower() == "done":
            break
        elif item:
            shopping_list.append(item)

    shopping_list.sort()
    print("Your shopping list:", shopping_list)


main()
