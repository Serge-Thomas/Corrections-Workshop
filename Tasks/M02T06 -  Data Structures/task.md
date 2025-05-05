# Data Structures - Shopping List Task

## Auto-graded Task 1: Shopping List Manager

1. Write a Python program called `shopping_list.py` that creates a shopping list application.
2. The program should allow the user to add items to a shopping list until they enter the word "done".
3. When the user enters "done", the program should print out the complete shopping list in alphabetical order.
4. Example program run (what should show up in the Python console when you run it):
```
Enter item to add to shopping list (or 'done' to finish): <user enters apple>
Enter item to add to shopping list (or 'done' to finish): <user enters bread>
Enter item to add to shopping list (or 'done' to finish): <user enters milk>
Enter item to add to shopping list (or 'done' to finish): <user enters done>
Your shopping list: ['apple', 'bread', 'milk']
```

HINT: When comparing user input to "done", you can use `.lower()` to eliminate case sensitivity.

## Auto-graded Task 2: Grocery Store Inventory

Imagine you are managing a small grocery store. You would like to calculate the total value of your inventory.

1. Create a new Python file in your folder called `grocery_store.py`.
2. Create a list called `inventory` that should contain at least five items sold in the grocery store.
3. Next, create a dictionary called `quantity` that should contain the quantity available for each item in your inventory.
4. Create another dictionary called `price` that should contain the price for each item in your inventory.
5. Next, calculate the total value of the inventory in the store and store the results inside a variable called `total_value`. You will need to loop through the appropriate dictionaries and lists to do this.
   * Tip: When you loop through the inventory list, the "items" can be used as keys to access the corresponding "quantity" and "price" values. Each "item_value" is calculated by multiplying the quantity by the price. For example: `item_value = (quantity[item] * price[item])`
6. Additionally, identify and print the most expensive item in your inventory.
7. Finally, print out the result of your total inventory value calculation.

## Challenge

Use this opportunity to extend yourself by completing an optional challenge activity.

1. Create a new file in this folder called `shopping_budget.py`.
2. Create a program that asks the user to input their shopping budget.
3. Then, allow the user to add items and their prices to a shopping list.
4. As items are added, show the user how much of their budget remains.
5. If they exceed their budget, inform them and ask if they want to remove an item.
6. When they're done shopping (by entering "checkout"), show them their final list and how much of their budget they've spent or have left over.

Hint: You will need to use dictionaries to store both the items and their prices, and possibly a list to maintain the order of items added.