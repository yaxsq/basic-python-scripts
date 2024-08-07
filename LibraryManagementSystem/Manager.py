from Library import Library
from Book import Book

if __name__ == "__main__":
    book = Book("amog us", "Sloth")
    print(book)

    library = Library()
    library.add_book("amog us", "sloth")
    library.add_book("book 2", "author 1")
    library.display_books()         # should output the two books added above

    library._add_random_books()     # checking if method is accessible // it is
    library.display_books()

    library.remove_book("book 2", "author")
    library.display_books()         # should not remove anything and print book not found

    library.remove_book("Book 2", "Author 1")
    library.display_books()         # should remove Book 2 from the random books

    library.remove_book("book 2", "author 1")
    library.display_books()         # should remove book 2 from the book added above
