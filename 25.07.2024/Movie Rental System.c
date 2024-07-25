#include <stdio.h>
#include <stdlib.h>
struct Movie {
    char title[100];
    char genre[50];
    double rentalPrice;
};
double calculateTotalRentalCost(struct Movie rentedMovies[], int numMovies, int rentalPeriodInDays) {
    double totalCost = 0.0;
    for (int i = 0; i < numMovies; i++) {
        totalCost += rentedMovies[i].rentalPrice * rentalPeriodInDays;
    }
    return totalCost;
}
int main() {
    struct Movie rentedMovies[] = {
        {"Inception", "Sci-Fi", 2.5},
        {"The Dark Knight", "Action", 3.0},
        {"Pulp Fiction", "Crime", 2.0}
    };
    int numMovies = sizeof(rentedMovies) / sizeof(rentedMovies[0]);
    int rentalPeriodInDays = 7;
    double totalCost = calculateTotalRentalCost(rentedMovies, numMovies, rentalPeriodInDays);
    printf("Total rental cost: $%.2lf\n", totalCost);

    return 0;
}
