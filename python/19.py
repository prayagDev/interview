class Book:
    
    total_book_count = 0
    
    def __init__(self, title, author, isbn):
        if not Book.is_valid_isbn(isbn):
            raise ValueError("Invalid ISBN! ISBN must contain exactly 13 digits.")
        
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        
        Book.total_book_count += 1
        
    def borrow(self):
        if self.is_borrowed:
            print(f'"{self.title}" is already borrowed.')
        else:
            self.is_borrowed = True
            print(f'You borrowed "{self.title}".')

    def return_book(self):
        if not self.is_borrowed:
            print(f'"{self.title}" is already available.')
        else:
            self.is_borrowed = False
            print(f'You returned "{self.title}".')
            
    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"

        print("-" * 35)
        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"ISBN   : {self.isbn}")
        print(f"Status : {status}")
        print("-" * 35)
    
    @classmethod
    def from_string(cls, data):
        title, author, isbn = data.split(";")
        return cls(title, author, isbn)
        
    @classmethod
    def total_books(cls):
        return cls.total_book_count
    
    @staticmethod
    def is_valid_isbn(isbn):
        return isbn.isdigit() and len(isbn) == 13
        

book1 = Book(
    "Python Crash Course",
    "Eric Matthes",
    "9781593279288"
)

book2 = Book.from_string(
    "Atomic Habits;James Clear;9780735211292"
)

print("Total Books:", Book.total_books())

print()

print("Checking ISBNs")
print(Book.is_valid_isbn("9780735211292"))  # True
print(Book.is_valid_isbn("12345"))          # False

print()

book1.borrow()
book1.borrow()

print()

book1.return_book()
book1.return_book()

print()

book1.display()
book2.display()

