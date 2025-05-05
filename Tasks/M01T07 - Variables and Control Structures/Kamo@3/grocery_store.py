# List of items in the grocery store
inventory = [
    "apples",
    "bananas",
    "milk",
    "mango",
    "eggs",
]

# Dictionary of quantities for each item
quantity = {
    "apples": 50,
    "bananas": 30,
    "milk": 20,
    "mango": 15,
    "eggs": 100,

}

# Dictionary for each item.
price = {
    "apples": 5.00,
    "bananas": 11.00,
    "milk": 25.00,
    "mango": 7.00,
    "eggs": 45.00,

}

# Calculate total inventory value
total_value = 0
for item in inventory:
    item_value = quantity[item] * price[item]
    total_value += item_value

# Identifying the most expensive item.
most_expensive_item = max(price, key=price.get)

# Printing results
print(f"Total inventory value: R{total_value:2f}")
print(f"Most expensive item: {most_expensive_item} at R:{price[most_expensive_item]:.2f}")
