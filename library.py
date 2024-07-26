from book import Book


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, genre, description):
        book = Book(book_id, title, author, genre, description)
        self.books[book_id] = book

    def search_book(self, title):
        for book_id, book in self.books.items():
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title, username):
        book = self.search_book(title)
        if book:
            if book.checked_out_by is None:
                book.checked_out_by = username
                return True, f"You have successfully checked out {book.title}."
            else:
                return False, f"Sorry, the book is already checked out by {book.checked_out_by}."
        return False, "Sorry, the book is not available in the library."

    def return_book(self, title, username):
        book = self.search_book(title)
        if book:
            if book.checked_out_by == username:
                book.checked_out_by = None
                return True, f"You have successfully returned {book.title}."
            else:
                return False, "Sorry, you cannot return a book that you haven't checked out."
        return False, "Sorry, the book is not available in the library."
