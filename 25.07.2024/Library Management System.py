#Scenario:
#You are developing a library management system. 
#Each book has a title, author, and availability status.
#Implement a function to borrow a book.

#Code:
class Book:
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available

def borrow_book(book):
    if book.is_available:
        book.is_available = False
        print("Book borrowed successfully")
    else:
        print("Book is not available")
book = Book("The Great Gatsby", "F. Scott Fitzgerald", True)
borrow_book(book)
print(book.is_available)  
