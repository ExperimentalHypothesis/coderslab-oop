import isbnlib

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        if not Book.check_isbn(isbn):
            raise ValueError("invalid ISBN")
        self.isbn = isbn

    @staticmethod
    def check_isbn(isbn):
        return isbnlib.is_isbn10(isbn) or isbnlib.is_isbn13(isbn)