# Restaurant menu



restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = "Cream_soda: 3.25", "Orange_juice: 2.99"
print(restaurant_menu)

restaurant_menu.update({"Steak": "17.99"})
print(restaurant_menu)
