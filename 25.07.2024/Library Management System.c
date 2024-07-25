#include <stdio.h>
#include <stdbool.h>
struct Book {
    int id;
    char title[100];
    char author[100];
    bool isBorrowed;
};
void borrowBook(struct Book *book) {
    if (!book->isBorrowed) {
        book->isBorrowed = true;
        printf("Book \"%s\" borrowed successfully!\n", book->title);
    } else {
        printf("Sorry, this book is already borrowed.\n");
    }
}
int main() {
    struct Book myBook = {1, "The Great Gatsby", "F. Scott Fitzgerald", false};
    borrowBook(&myBook);
    return 0;
}
