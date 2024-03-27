# Global list to store books
books = []

def add_book(title, author, isbn):
    books.append({"title": title, "author": author, "isbn": isbn})

def list_books():
    for book in books:
        print(book)


from storage import Storage
from models import Book

class BookManager:
    def __init__(self):
        self.storage = Storage()

    def add_book(self, book:Book):
        self.storage.cursor.execute("INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)",
                                     (book.title, book.author, book.isbn))
        self.storage.conn.commit()

    def update_book(self,book:Book):
        # Update an existing book
        self.storage.cursor.execute("UPDATE books SET title=?, author=? WHERE isbn=?",
                                     (book.title, book.author, book.isbn))
        self.storage.conn.commit()

    def delete_book(self,book_isbn):
        # Delete a book from storage
        self.storage.cursor.execute("DELETE FROM books WHERE isbn=?", (book_isbn,))
        self.storage.conn.commit()

    def list_books(self):
        # List all books
        self.storage.cursor.execute("SELECT * FROM books")
        books = self.storage.cursor.fetchall()
        return books

    def search_book(self, keyword):
        # Search for a book by title, author, or ISBN
        self.storage.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?",
                                     ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        books = self.storage.cursor.fetchall()
        return books

    def close_connection(self):
        self.storage.close_connection()


