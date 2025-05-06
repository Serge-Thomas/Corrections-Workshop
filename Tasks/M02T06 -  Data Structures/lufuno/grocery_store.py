# inventory list with unique items
inventory = [
    "amasi", "chakalaka", "samp", "koeksisters", "naartjies",
    "biltong", "boerewors", "rooibos_tea", "pap", "vetkoek"
]

# Quantities for each item
quantity = {
    "amasi": 35,
    "chakalaka": 20,
    "samp": 50,
    "koeksisters": 60,
    "naartjies": 80,
    "biltong": 25,
    "boerewors": 30,
    "rooibos_tea": 40,
    "pap": 45,
    "vetkoek": 70
}

# Prices for each item (in Rands)
price = {
    "amasi": 22.00,
    "chakalaka": 18.50,
    "samp": 12.00,
    "koeksisters": 5.00,
    "naartjies": 3.50,
    "biltong": 150.00,
    "boerewors": 85.00,
    "rooibos_tea": 30.00,
    "pap": 10.00,
    "vetkoek": 6.00
}

# Calculate total inventory value and find most expensive item
total_value = 0
most_expensive_item = ""
highest_price = 0

for item in inventory:
    item_value = quantity[item] * price[item]
    total_value += item_value

    if price[item] > highest_price:
        highest_price = price[item]
        most_expensive_item = item

# Print results
print(f"Total inventory value: R{total_value:.2f}")
print(f"Most expensive item: {most_expensive_item.replace('_', ' ').title()} \
(R{highest_price:.2f})")
