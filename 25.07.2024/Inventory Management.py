#Scenario:
#You are managing an inventory system for a small shop.
#Each product has a name, quantity, and price.
#Implement a function to update the quantity of a product after a sale.

#Code:
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

def update_quantity(product, sold_quantity):
    if sold_quantity <= product.quantity:
        product.quantity -= sold_quantity
    else:
        print("Not enough stock")

# Example usage
product = Product("Laptop", 10, 1000)
update_quantity(product, 3)
print(product.quantity)  # Output: 7
