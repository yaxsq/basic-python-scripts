class Book:
    title = ""
    author = ""
    available = False

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow_Book(self):
        if self.available == True:
            self.available = False
            print(f"{self.title} is being borrowed")

    def return_Book(self):
        if self.available == False:         # Can also use > not self.available
            self.available = True;
            print(f"{self.title} has been returned")
