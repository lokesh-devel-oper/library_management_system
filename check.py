checkouts = []

def checkout_book(user_id, isbn):
    checkouts.append({"user_id": user_id, "isbn": isbn})


from storage import Storage
from models import Transaction

class CheckInOut:
    def __init__(self):
        self.storage = Storage()

    def check_in(self, transaction):
        self.storage.cursor.execute("INSERT INTO transactions (user_id, book_isbn, transaction_type, transaction_date) VALUES (?, ?, ?, ?)",
                                     (transaction.user_id, transaction.book_isbn, "check_in", transaction.transaction_date))
        self.storage.conn.commit()

    def check_out(self, user_id, book_isbn):
        # Check in a book from a user
        # Find the latest transaction for the specified book and user
        self.storage.cursor.execute("SELECT id FROM transactions WHERE user_id=? AND book_isbn=? AND transaction_type='check_out' ORDER BY transaction_date DESC LIMIT 1",
                                     (user_id, book_isbn))
        row = self.storage.cursor.fetchone()
        if row:
            transaction_id = row[0]
            # Update the transaction to mark it as checked in
            self.storage.cursor.execute("UPDATE transactions SET transaction_type='check_in' WHERE id=?",
                                         (transaction_id,))
            self.storage.conn.commit()
        else:
            print("No check-out record found for the specified user and book.")

    def track_availability(self, book):
        # Track the availability of a book
        pass

    def close_connection(self):
        self.storage.close_connection()

