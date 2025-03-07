package net.javaguides.lms;
public class Book {
    private int id;
    private String title;
    private String author;
    private boolean isBorrowed;
    public void borrowBook() {
        if (!isBorrowed) {
            isBorrowed = true;
            System.out.println("Book \"" + title + "\" borrowed successfully!");
        } else {
            System.out.println("Sorry, this book is already borrowed.");
        }
    }
    public static void main(String[] args) {
        Book myBook = new Book(1, "The Great Gatsby", "F. Scott Fitzgerald");
        myBook.borrowBook();
    }
}
