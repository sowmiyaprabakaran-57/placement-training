#Scenario:
#You are building a movie rental system where customers can rent movies. 
#Each movie has a title, genre, and rental price. 
#You need to create a function to calculate the total rental cost for a customer given a list of rented movies and the rental period.


#Code:
class Movie:
    def __init__(self, title, genre, rental_price):
        self.title = title
        self.genre = genre
        self.rental_price = rental_price

def calculate_rental_cost(movies, rental_days):
    total_cost = 0
    for movie in movies:
        total_cost += movie.rental_price * rental_days
    return total_cost

# Example usage
movies = [Movie("Movie A", "Action", 3.5), Movie("Movie B", "Comedy", 2.5)]
rental_days = 3
print(calculate_rental_cost(movies, rental_days))  # Output: 18.0
