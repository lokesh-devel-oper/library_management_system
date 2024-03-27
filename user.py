users = []

def add_user(name, user_id):
    users.append({"name": name, "user_id": user_id})


from storage import Storage
from models import User

class UserManager:
    def __init__(self):
        self.storage = Storage()

    def add_user(self, user:User):
        self.storage.cursor.execute("INSERT INTO users (name, user_id) VALUES (?, ?)",
                                     (user.name, user.user_id))
        self.storage.conn.commit()

    def update_user(self, user:User):
        # Update an existing user
        self.storage.cursor.execute("UPDATE users SET name=? WHERE user_id=?",
                                     (user.name, user.user_id))
        self.storage.conn.commit()

    def delete_user(self, user_id):
        # Delete a user from storage
        self.storage.cursor.execute("DELETE FROM users WHERE user_id=?", (user_id,))
        self.storage.conn.commit()

    def list_users(self):
        # List all users
        self.storage.cursor.execute("SELECT * FROM users")
        users = self.storage.cursor.fetchall()
        return users

    def search_user(self, keyword):
        # Search for a user by name or user ID
        self.storage.cursor.execute("SELECT * FROM users WHERE name LIKE ? OR user_id LIKE ?",
                                     ('%' + keyword + '%', '%' + keyword + '%'))
        users = self.storage.cursor.fetchall()
        return users

    def close_connection(self):
        self.storage.close_connection()

