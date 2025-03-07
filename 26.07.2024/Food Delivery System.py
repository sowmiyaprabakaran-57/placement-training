class Order:
    def __init__(self, customer_name, food_items, total_cost):
        self.customer_name = customer_name
        self.food_items = food_items
        self.total_cost = total_cost
def average_order_cost(orders):
    return sum(order.total_cost for order in orders) / len(orders) if orders else 0
orders = [Order("Alice", ["Pizza", "Soda"], 20.0), Order("Bob", ["Burger", "Fries"], 15.0)]
print(average_order_cost(orders)) 
