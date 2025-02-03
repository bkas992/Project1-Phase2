def run_tests():
    inventory = Inventory()

    print("\n### Adding Products ###")
    inventory.add_product(101, "Laptop", 800, 10, "Electronics")
    inventory.add_product(102, "Smartphone", 500, 15, "Electronics")
    inventory.add_product(103, "Headphones", 50, 50, "Accessories")
    inventory.add_product(104, "Keyboard", 40, 30, "Accessories")

    print("\n### Display Inventory ###")
    print(inventory.display_inventory())

    print("\n### Searching Products ###")
    print(inventory.search_product(101))  # Search by ID
    print(inventory.search_product("Smartphone"))  # Search by name

    print("\n### Finding Cheapest Product ###")
    print(inventory.find_cheapest_product())

    print("\n### Finding Product with Highest Stock ###")
    print(inventory.find_highest_stock())

    print("\n### Updating Product Quantity ###")
    inventory.update_quantity(102, 5)
    print(inventory.display_inventory())

    print("\n### Removing a Product ###")
    inventory.remove_product(103)
    print(inventory.display_inventory())

    print("\n### Finding Cheapest Product after Removal ###")
    print(inventory.find_cheapest_product())

    print("\n### Finding Product with Highest Stock after Removal ###")
    print(inventory.find_highest_stock())

# Run all test cases
run_tests()
