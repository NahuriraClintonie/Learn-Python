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
        # Cancel a booking
        booked_seats = seat.get_booked_seats()
        if not booked_seats:
            print("There are no booked seats to cancel.")
        else:
            print("Booked Seats:", ", ".join(booked_seats))
            seat_number = input("Enter the seat number to cancel: ")
            if seat_number in booked_seats:
                confirmation = input(f"Are you sure you want to cancel seat {seat_number}? (yes/no): ").lower()
                if confirmation == 'yes':
                    result = seat.cancel_seat(seat_number)
                    print(result)
                else:
                    print("Cancellation aborted.")
            else:
                print(f"Seat {seat_number} is not currently booked.")
    elif choice == '4':
        # View all bookings
        booked_seats = seat.get_booked_seats()
        if booked_seats:
            print("\nAll Booked Seats:", ", ".join(booked_seats))
        else:
            print("\nNo seats are currently booked.")
    elif choice == '5':
        print("\nLogging out... Goodbye!")
        return False  # To indicate exit
    else:
        print("\nInvalid choice. Please select a valid option.")
    
    return True  # To keep the program running

def main_menu():
    """Main menu loop to keep displaying the menu and handling choices."""
    while True:
        view.display_menu()
        choice = input("Enter your choice (1-5): ")
        if not handle_user_choice(choice):
            break
