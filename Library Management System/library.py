# Initialize sets and dictionaries
available_books = set()
borrowed_books = set()
members = {}  # Maps member names to the books they've borrowed

def add_book(title, author, year):
    """Add a new book to the library."""
    book = (title, author, year)
    if book in available_books or book in borrowed_books:
        print(f"The book '{title}' is already in the library.")
    else:
        available_books.add(book)
        print(f"Book '{title}' added successfully.")

def borrow_book(member_name, title):
    """Allow a member to borrow a book if available."""
    book = next((b for b in available_books if b[0] == title), None)
    if book:
        available_books.remove(book)
        borrowed_books.add(book)
        if member_name in members:
            members[member_name].append(book)
        else:
            members[member_name] = [book]
        print(f"{member_name} borrowed '{title}'.")
    else:
        print(f"The book '{title}' is either unavailable or does not exist.")

def return_book(member_name, title):
    """Allow a member to return a borrowed book."""
    if member_name not in members:
        print(f"No records found for member '{member_name}'.")
        return
    
    borrowed_books_by_member = members[member_name]
    book = next((b for b in borrowed_books_by_member if b[0] == title), None)
    
    if book:
        borrowed_books_by_member.remove(book)
        borrowed_books.remove(book)
        available_books.add(book)
        
        if not borrowed_books_by_member:
            del members[member_name]
        
        print(f"{member_name} returned '{title}'.")
    else:
        print(f"{member_name} has not borrowed the book '{title}'.")

def view_available_books():
    """Display all available books in the library."""
    if available_books:
        print("Available Books:")
        for book in available_books:
            print(f"- {book[0]} by {book[1]} ({book[2]})")
    else:
        print("No books are currently available.")

def view_borrowed_books():
    """Display all borrowed books and who borrowed them."""
    if borrowed_books:
        print("Borrowed Books:")
        for member, books in members.items():
            print(f"{member} has borrowed:")
            for book in books:
                print(f"  - {book[0]} by {book[1]} ({book[2]})")
    else:
        print("No books are currently borrowed.")

# Main menu
def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add a New Book")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. View Available Books")
        print("5. View Borrowed Books")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter book year of publication: ")
            add_book(title, author, year)
        elif choice == "2":
            member_name = input("Enter member's name: ")
            title = input("Enter the title of the book to borrow: ")
            borrow_book(member_name, title)
        elif choice == "3":
            member_name = input("Enter member's name: ")
            title = input("Enter the title of the book to return: ")
            return_book(member_name, title)
        elif choice == "4":
            view_available_books()
        elif choice == "5":
            view_borrowed_books()
        elif choice == "6":
            print("Exiting the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
