class Book:
    def __init__(self, book_id, title, author, genre, description):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
        self.checked_out_by = None  # None means the book is available

    def __str__(self):
        status = "Available" if self.checked_out_by is None else f"Checked out by {self.checked_out_by}"
        return f"{self.title} by {self.author}, Genre: {self.genre}, Description: {self.description}, Status: {status}"

    def calculate_duration(self):
        if self.checked_out_time and self.returned_time:
            duration = self.returned_time - self.checked_out_time
            return duration
        return None