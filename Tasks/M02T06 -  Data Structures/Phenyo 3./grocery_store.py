# Create inventory list
inventory = ["apples", "bananas", "bread", "milk", "eggs"]

# Dictionary of quantities using a loop
quantity = {}
for item in inventory:
    qty = int(input(f"Enter quantity for {item}: "))
    quantity[item] = qty  # Store quantity in the dictionary.
    print(f"Quantity for {item} is: {qty}")


# Dictionary of prices using a loop
price = {}
for item in inventory:
    prc = float(input(f"Enter price for {item}: "))
    price[item] = prc

# Calculate total value
total_value = 0
for item in inventory:
    item_value = quantity[item] * price[item]
    total_value += item_value

# Identify the most expensive item
most_expensive_item = max(price, key=price.get)

# Print results
print(f"\nThe total inventory value is: R{total_value:.2f}")
print(f"The most expensive item is: {most_expensive_item} "
      f"at R{price[most_expensive_item]:.2f}")
