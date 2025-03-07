class ParkingSpot:
    def __init__(self, spot_number, vehicle_type, parking_fee):
        self.spot_number = spot_number
        self.vehicle_type = vehicle_type
        self.parking_fee = parking_fee

def total_parking_fee(spots, vehicle_type):
    return sum(spot.parking_fee for spot in spots if spot.vehicle_type == vehicle_type)
spots = [ParkingSpot(1, "Car", 5), ParkingSpot(2, "Bike", 2), ParkingSpot(3, "Car", 6)]
print(total_parking_fee(spots, "Car"))  
