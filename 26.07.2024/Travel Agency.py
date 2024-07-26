class Trip:
    def __init__(self, destination, duration, cost):
        self.destination = destination
        self.duration = duration
        self.cost = cost
def average_trip_cost(trips, destination):
    destination_costs = [trip.cost for trip in trips if trip.destination == destination]
    return sum(destination_costs) / len(destination_costs) if destination_costs else 0
trips = [Trip("Paris", 7, 1500), Trip("Paris", 5, 1200), Trip("London", 4, 1000)]
print(average_trip_cost(trips, "Paris"))  
