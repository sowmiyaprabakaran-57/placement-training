class Booking:
    def __init__(self, flight_number, passenger_name, ticket_price):
        self.flight_number = flight_number
        self.passenger_name = passenger_name
        self.ticket_price = ticket_price
def total_ticket_sales(bookings, flight_number):
    return sum(booking.ticket_price for booking in bookings if booking.flight_number == flight_number)
bookings = [Booking("AA123", "Alice", 300), Booking("AA123", "Bob", 350), Booking("BB456", "Charlie", 400)]
print(total_ticket_sales(bookings, "AA123"))  
