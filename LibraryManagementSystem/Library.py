# from array import array
from Book import Book


class Library:
    # books = array()
    books = []

    def __init__(self):
        self.books = []

    # creates then adds a new book object in the books list
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    # def _validate(self, book):
    #     if not isinstance(book, Book):
    #         raise TypeError("__validate__: Incorrect object type")

    # searches then returns a book

    def _get_book(self, title: str, author: str) -> Book:
        for book in self.books:
            if book.title.lower() == title.lower() and book.author.lower() == author.lower():
                return book
        return None  # Try without this

    # gets the book from _get_book method and removes it from the list
    def remove_book(self, title: str, author: str):
        temp_book = self._get_book(title, author)
        if temp_book is None:
            print("Book not found")
            return
        self.books.remove(temp_book)

    # prints the list with one book in every line
    def display_books(self):
        # print(self.books)
        print("** AVAILABLE BOOKS **")
        for book in self.books:
            print(book)
            # print(f"{book.title}, {book.author}")
        print()

    # gets the book from the list then updates the availability
    def borrow_book(self, title: str, author: str):
        temp_book = self._get_book(title, author)
        if temp_book is None:
            print("Book not found")
        else:
            temp_book.borrow_book()

        # if not temp_book.available:
        #     print("Book is not available")
        # else:
        # temp_book.available = False
        # print("You have now borrowed this book")

    # gets the book from the list then updates the availability
    def return_book(self, title: str, author: str):
        temp_book = self._get_book(title, author)
        if temp_book is None:
            print("Book not found")
        else:
            temp_book.return_book()

        # if temp_book.available:
        #     print("Book has not been borrowed")
        # else:
        #     temp_book.available = True
        #     print("You have now returned this book")

    # testing type check // adding books
    def _add_random_books(self):
        self.add_book("Book 1", "Author 1")
        self.add_book("Book 2", "Author 1")
        self.add_book("Book 3", "Author 2")
        self.add_book("Book 4", "Author 3")
