import sqlite3

class Storage:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                author TEXT,
                                isbn TEXT
                                )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                user_id TEXT
                                )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                                id INTEGER PRIMARY KEY,
                                user_id INTEGER,
                                book_isbn TEXT,
                                transaction_type TEXT,
                                transaction_date TEXT,
                                FOREIGN KEY (user_id) REFERENCES users(id),
                                FOREIGN KEY (book_isbn) REFERENCES books(isbn)
                                )''')
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
