class Car:
    def __init__(self, model, rental_rate_per_day, is_available):
        self.model = model
        self.rental_rate_per_day = rental_rate_per_day
        self.is_available = is_available

def total_rental_income(cars, rental_days):
    return sum(car.rental_rate_per_day * rental_days for car in cars if not car.is_available)
cars = [Car("Toyota", 40, False), Car("Honda", 50, True), Car("Ford", 60, False)]
print(total_rental_income(cars, 3))  
