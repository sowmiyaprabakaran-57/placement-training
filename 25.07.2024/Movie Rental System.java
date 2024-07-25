import java.util.List;

class Movie {
    private String title;
    private String genre;
    private double rentalPrice;

    public Movie(String title, String genre, double rentalPrice) {
        this.title = title;
        this.genre = genre;
        this.rentalPrice = rentalPrice;
    }
    @Override
    public String toString() {
        return title + " (" + genre + ")";
    }
}

public class MovieRentalSystem {
    public static double calculateTotalRentalCost(List<Movie> rentedMovies, int rentalPeriodInDays) {
        double totalCost = 0.0;
        for (Movie movie : rentedMovies) {
            totalCost += movie.getRentalPrice() * rentalPeriodInDays;
        }
        return totalCost;
    }
    public static void main(String[] args) {
        List<Movie> rentedMovies = List.of(
                new Movie("Inception", "Sci-Fi", 2.5),
                new Movie("The Dark Knight", "Action", 3.0),
                new Movie("Pulp Fiction", "Crime", 2.0)
        );
        int rentalPeriodInDays = 7;
        double totalCost = calculateTotalRentalCost(rentedMovies, rentalPeriodInDays);
        System.out.println("Total rental cost: $" + totalCost);
    }
}
