import heapq

class Product:
    def __init__(self, product_id, name, price, quantity, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def __lt__(self, other):
        """This is for priority queue sorting (lowest price first)"""
        return self.price < other.price

class Inventory:
    def __init__(self):
        self.products = {}  # Dictionary to store products (product_id -> Product object)
        self.price_heap = []  # Min-Heap to track cheapest product
        self.stock_heap = []  # Max-Heap to track highest stock (negative quantity for max heap)

    def add_product(self, product_id, name, price, quantity, category):
        """Adds a new product to the inventory."""
        if product_id in self.products:
            print(f"Product ID {product_id} already exists.")
            return
        
        product = Product(product_id, name, price, quantity, category)
        self.products[product_id] = product
        
        heapq.heappush(self.price_heap, product)  # Insert into min-heap (cheapest product)
        heapq.heappush(self.stock_heap, (-quantity, product))  # Insert into max-heap (highest stock)

    def remove_product(self, product_id):
        """Removes a product from inventory."""
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product {product_id} removed.")
        else:
            print(f"Product ID {product_id} not found.")

    def search_product(self, identifier):
        """Searches for a product by ID or name."""
        for product in self.products.values():
            if product.product_id == identifier or product.name.lower() == identifier.lower():
                return vars(product)
        return "Product not found."

    def find_cheapest_product(self):
        """Finds the cheapest product."""
        while self.price_heap:
            product = self.price_heap[0]  # Peek at the heap
            if product.product_id in self.products:
                return vars(product)
            heapq.heappop(self.price_heap)  # Remove outdated products
        return "No products available."

    def find_highest_stock(self):
        """Finds the product with the highest stock."""
        while self.stock_heap:
            quantity, product = self.stock_heap[0]  # Peek at the heap
            if product.product_id in self.products:
                return vars(product)
            heapq.heappop(self.stock_heap)  # Remove outdated products
        return "No products available."

    def update_quantity(self, product_id, new_quantity):
        """Updates the quantity of a product."""
        if product_id in self.products:
            self.products[product_id].quantity = new_quantity
            heapq.heappush(self.stock_heap, (-new_quantity, self.products[product_id]))  # Update max-heap
            print(f"Quantity updated for Product {product_id}.")
        else:
            print("Product not found.")

    def display_inventory(self):
        """Displays all products in inventory."""
        return [vars(product) for product in self.products.values()]
    