#Scenario:
#You are building an online shopping cart system.
#Each cart contains multiple items, each with a name, quantity, and price. 
#Implement a function to calculate the total cost of the items in the cart.

#Code:
class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

def calculate_total_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost += item.quantity * item.price
    return total_cost
cart = [Item("Apple", 2, 1.5), Item("Banana", 3, 0.75)]
print(calculate_total_cost(cart))  # Output: 6.75
