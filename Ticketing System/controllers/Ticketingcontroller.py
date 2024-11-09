import views.view as view
import models.Seat as seat

def handle_user_choice(choice):
    "Handle user choices and call the appropriate function."
    if choice == '1':
        # View available seats
        available_seats = seat.get_available_seats()
        if available_seats:
            print("Available Seats:", ", ".join(available_seats))
        else:
            print("All seats are currently booked.")
    elif choice == '2':
        seat_number = input("Enter the seat number to book (e.g., A1, B2): ")
        result = seat.book_seat(seat_number)  # Call the book_seat function
        print(result)  # Display the booking result to the user
    elif choice == '3':
        # Placeholder for cancel booking functionality
        print("You selected: Cancel a Booking (Functionality coming soon)")
    elif choice == '4':
        # Placeholder for view all bookings functionality
        print("You selected: View All Bookings (Functionality coming soon)")
    elif choice == '5':
        print("Logging out... Goodbye!")
        return False  # To indicate exit
    else:
        print("Invalid choice. Please select a valid option.")
    
    return True  # To keep the program running

def main_menu():
    """Main menu loop to keep displaying the menu and handling choices."""
    while True:
        view.display_menu()
        choice = input("Enter your choice (1-5): ")
        if not handle_user_choice(choice):
            break
