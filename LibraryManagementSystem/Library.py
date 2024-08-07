# from array import array
from Book import Book

class Library:
    # books = array()
    books = []
    def __init__(self):
        self.books = []

    def add_Book(self, title, author):
        book = Book(title, author)


    def __validate__(self, book):
        if not isinstance(book, Book):
            raise TypeError("__validate__: Incorrect object type")

