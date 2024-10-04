class Book:
    def __init__(self, title, author) -> None:
        self.title = title 
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out 
    
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self) -> None:
        self._books = list()

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {book}")
                return
        print(f"Book '{title}' is either not available or does not exist in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {book}")
                return
            
        print(f"Book '{title}' is either not checked out or does not exist in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
           for book in available_books:
               print(book)
        else:
           print('No available books at the moment.')