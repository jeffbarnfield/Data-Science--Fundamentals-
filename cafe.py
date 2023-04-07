# Create 1 list and 2 dictionaries
menu = ["Croissant", "Carrot Cake", "Apple", "Cheese Toastie"]
stock = {"Croissant": 5, "Carrot Cake": 10, "Apple": 6, "Cheese Toastie": 3}
price = {"Croissant": 1.25, "Carrot Cake": 3.50, "Apple": 0.80, "Cheese Toastie": 4.50}

# Calculate the total stock value of all menu items
total_stock = 0

# Iterate through all items on the menu, calculate each item value and add to the total stock value
for items in menu:
    item_value = stock[items] * price[items]
    total_stock += item_value

# Total Stock Value in GBP
print(f"Total Stock Value: £ {total_stock:.2f}")