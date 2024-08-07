from Library import Library
from Book import Book

if __name__ == "__main__":
    book = Book("amog us", "Sloth")
    print(book, "\n")

    library = Library()
    library.add_book("amog us", "sloth")
    library.add_book("book 2", "author 1")
    print("# should output the two books added above")
    library.display_books()

    library._add_random_books()
    print("# checking if method is accessible // it is")
    library.display_books()


    library.remove_book("book 2", "author")
    print("# should not remove anything and print book not found")
    library.display_books()

    library.remove_book("Book 2", "Author 1")
    print("# should remove Book 2 from the random books")
    library.display_books()
    # This does not result in book 2 from random books being deleted
    # This must be due to the titles being compared in lowercase

    library.remove_book("book 2", "author 1")
    print("# should remove book 2 from the book added above")
    library.display_books()

    # Since the titles are compared in lowercase, the book added in the random books is deleted
    # This is because of the remove function being sequential
    # This can be easily fixed by changing the comparison to be case-sensitive // removing the .lower() function


    library.borrow_book("book 3", "aithor 3")
    print("# should change nothing and print book not found")
    library.display_books()

    library.borrow_book("book 3", "author 2")
    print("# should set availablity to False")
    library.display_books()

    library.borrow_book("book 3", "author 2")
    print("# should print book is borrowed already")
    library.display_books()


    library.return_book("Book 3", "authir 2")
    print("# should print book not found")
    library.display_books()

    library.return_book("Book 3", "Author 2")
    print("# should return the book")
    library.display_books()

    library.return_book("Book 3", "author 2")
    print("# should say the book was not borrowed")
    library.display_books()
