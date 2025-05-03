# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0 

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

book1 = Book("The Alchemist")
book2 = Book("1984")
book3 = Book("To Kill a Mockingbird")
print("Total books:", Book.total_books)
