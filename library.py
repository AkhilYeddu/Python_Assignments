from datetime import datetime, timedelta

# Catalog Management
catalog = {
    "001": {"title": "Python Programming", "author": "John Smith", "quantity": 5},
    "002": {"title": "Data Structures", "author": "Alice Johnson", "quantity": 3},
    "003": {"title": "Machine Learning", "author": "Bob Brown", "quantity": 2}
}

# User Management
users = {}

# Transactions
transactions = {}

def display_catalog():
    print("Current Catalog:")
    for book_id, book_info in catalog.items():
        print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Available: {book_info['quantity']}")

def register_user(user_id, name):
    if user_id not in users:
        users[user_id] = {"name": name, "books_checked_out": {}}
        print(f"User {name} with ID {user_id} registered successfully!")
    else:
        print("User ID already exists!")

def checkout_book(user_id, book_id):
    if user_id in users and book_id in catalog:
        if len(users[user_id]["books_checked_out"]) < 3:
            if catalog[book_id]["quantity"] > 0:
                users[user_id]["books_checked_out"][book_id] = datetime.now()
                catalog[book_id]["quantity"] -= 1
                print(f"Book '{catalog[book_id]['title']}' checked out successfully by User ID {user_id}.")
            else:
                print("Book not available for checkout.")
        else:
            print("User has reached the maximum limit of checked out books.")
    else:
        print("Invalid user ID or book ID.")

def return_book(user_id, book_id):
    if user_id in users and book_id in users[user_id]["books_checked_out"]:
        return_date = datetime.now()
        checkout_date = users[user_id]["books_checked_out"].pop(book_id)
        catalog[book_id]["quantity"] += 1
        days_overdue = (return_date - (checkout_date + timedelta(days=14))).days
        if days_overdue > 0:
            fine = days_overdue
            print(f"Book '{catalog[book_id]['title']}' returned successfully with a fine of ${fine}.")
        else:
            print(f"Book '{catalog[book_id]['title']}' returned successfully.")
    else:
        print("Invalid user ID or book ID or book not checked out by user.")

def list_overdue_books(user_id):
    total_fine = 0
    if user_id in users:
        print(f"Overdue Books for User ID {user_id}:")
        for book_id, checkout_date in users[user_id]["books_checked_out"].items():
            days_overdue = (datetime.now() - (checkout_date + timedelta(days=14))).days
            if days_overdue > 0:
                fine = days_overdue
                total_fine += fine
                print(f"Book ID: {book_id}, Title: {catalog[book_id]['title']}, Overdue Days: {days_overdue}, Fine: ${fine}")
        print(f"Total Fine: ${total_fine}")
    else:
        print("Invalid user ID.")

# Example usage:
display_catalog()

register_user("101", "Alice")
register_user("102", "Bob")

checkout_book("101", "001")
checkout_book("101", "002")
checkout_book("101", "003")

return_book("101", "001")
return_book("101", "002")

checkout_book("101", "001")

list_overdue_books("101")