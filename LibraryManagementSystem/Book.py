class Book:
    title = ""
    author = ""
    available = False

    def __init__(self, title: str, author: str):
        # def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    # checks if the book is available and sets it to unavailable
    def borrow_book(self):
        if self.available == True:
            self.available = False
            print(f"{self.title} is being borrowed")
        else:
            print("Book not available")

    # checks if the book is not available and sets it to available
    def return_book(self):
        if self.available == False:  # Can also use > not self.available
            self.available = True;
            print(f"{self.title} has been returned")
        else:
            print("Book has not been borrowed")

    def __str__(self):
        return f"{self.title}, {self.author} " + "Availablility: " + str(self.available)
