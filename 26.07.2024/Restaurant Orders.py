class Order:
    def __init__(self, table_number, dishes, total_cost):
        self.table_number = table_number
        self.dishes = dishes
        self.total_cost = total_cost
def total_earnings(orders):
    return sum(order.total_cost for order in orders)
orders = [Order(1, ["Pizza", "Salad"], 25.0), Order(2, ["Pasta", "Soda"], 20.0)]
print(total_earnings(orders)) 
