class Reservation:
    def __init__(self, room_number, guest_name, number_of_nights, rate_per_night):
        self.room_number = room_number
        self.guest_name = guest_name
        self.number_of_nights = number_of_nights
        self.rate_per_night = rate_per_night
def total_reservation_income(reservations):
    return sum(reservation.number_of_nights * reservation.rate_per_night for reservation in reservations)
reservations = [Reservation(101, "Alice", 3, 100), Reservation(102, "Bob", 2, 150)]
print(total_reservation_income(reservations)) 
