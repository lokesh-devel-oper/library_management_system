class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class Transaction:
    def __init__(self, user_id, book_isbn, transaction_type, transaction_date):
        self.user_id = user_id
        self.book_isbn = book_isbn
        self.transaction_type = transaction_type
        self.transaction_date = transaction_date
