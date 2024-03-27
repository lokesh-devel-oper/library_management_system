from datetime import datetime
from book import BookManager
from user import UserManager
from check import CheckInOut
from models import Book, User, Transaction

def main():
    book_manager = BookManager()
    user_manager = UserManager()
    check_manager = CheckInOut()

    try:
        while True:
            print("Library Management System")
            print("1. Manage Books")
            print("2. Manage Users")
            print("3. Check Out/Check In Books")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                book_operation_menu(book_manager)
            elif choice == "2":
                user_operation_menu(user_manager)
            elif choice == "3":
                check_operation_menu(check_manager)
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("<<<<<<<<<<<  Invalid choice. Please try again.  >>>>>>>>>>>>>>>")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        book_manager.close_connection()
        user_manager.close_connection()
        check_manager.close_connection()

def user_operation_menu(user_manager:UserManager):
    try:
        while True:
            print("User Management")
            print("1. Add User")
            print("2. Update User")
            print("3. Delete User")
            print("4. List Users")
            print("5. Search User")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                user_name = input("Enter user name: ")
                user_id = input("enter your email: ")
                user_manager.add_user(User(user_name, user_id))
                print(f"-------------Successfully added {user_name}, Welcome!---------------")
            elif choice == "2":
                # Update User
                user_name = input("Enter user name: ")
                user_id = input("enter your email: ")
                user_manager.update_user(User(user_name, user_id))
                print(f"----------------Successfully updated {user_name}, Welcome!-------------")
            elif choice == "3":
                # Delete User
                user_id = input("enter your email: ")
                user_manager.delete_user(user_id)
                print(f"----------------Successfully Deleted user related with {user_id}----------")
            elif choice == "4":
                # List Users
                users = user_manager.list_users()
                print('*'*15)
                print(users)
                print("-"*15)
            elif choice == "5":
                # Search User
                keyword = input("enter name/email to search: ")
                users = user_manager.search_user(keyword)
                print('='*15)
                print(users)
                print("="*15)
            elif choice == "6":
                break
            else:
                print("---------------Invalid choice. Please try agin.----------------")
    except Exception as e:
        print(">>>>>>>>An error occurred:", str(e))

def check_operation_menu(check_manager: CheckInOut):
    try:
        while True:
            print("Check Out/Check In")
            print("1. Check Out")
            print("2. Check In")
            print("3. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Check Out
                user_id = input("enter your email: ")
                book_isbn = input("enter book isbn: ")
                check_manager.check_out(user_id, book_isbn)
                print('-------------------Checkout successfull----------------')
            elif choice == "2":
                # Check In
                user_id = input("enter your email: ")
                book_isbn = input("enter book isbn: ")
                check_manager.check_in(Transaction(user_id, book_isbn, 'check_in', datetime.now().strftime('%d/%m/%Y, %H:%M:%S')))
                print('-------------------checkin successful---------------------')
            elif choice == "3":
                break
            else:
                print("----------------Invalid choice. Please try again.------------")
    except Exception as e:
        print(">>>>>>>An error occurred:", str(e))

def book_operation_menu(book_manager: BookManager):
    try:
        while True:
            print("Book Management")
            print("1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. List Books")
            print("5. Search Book")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                book_title = input("enter book title: ")
                book_author = input('enter book author: ')
                book_isbn = input("enter book isbn: ")
                book_manager.add_book(Book(book_title,book_author,book_isbn))
                print(f"---------------Added {book_title} Successfully!------------------")
            elif choice == "2":
                # Update Book
                book_title = input("enter book title: ")
                book_author = input('enter book author: ')
                book_isbn = input("enter book isbn: ")
                book_manager.update_book(Book(book_title,book_author,book_isbn))
                print(f"----------------Updated {book_title} Successfully!-------------------")
            elif choice == "3":
                # Delete Book
                book_isbn = input("enter book isbn: ")
                book_manager.delete_book(book_isbn)
                print(f"------------------deleted book related with {book_isbn} Successfully!-------------")
            elif choice == "4":
                # List Books
                books = book_manager.list_books()
                print('*'*10)
                print(books)
                print("-"*10)
            elif choice == "5":
                # Search Book
                keyword = input("enter name/author/isbn to search: ")
                users = book_manager.search_book(keyword)
                print('='*10)
                print(users)
                print("="*10)
            elif choice == "6":
                break
            else:
                print("--------------------Invalid choice. Please try again.--------------------")
    except Exception as e:
        print(">>>>>>>>>An error occurred:", str(e))

# Implement other menu functions similarly

if __name__ == "__main__":
    main()
