# model.py

# List to store the booked seats
booked_seats = []

# List of all available seats (20 dummy seats for initialization)
all_seats = [
    "A1", "A2", "A3", "A4", "A5", 
    "B1", "B2", "B3", "B4", "B5",
    "C1", "C2", "C3", "C4", "C5",
    "D1", "D2", "D3", "D4", "D5"
]

def book_seat(seat_number):
    """
    Book a seat by adding it to the booked_seats list.
    """
    if seat_number in booked_seats:
        return f"Seat {seat_number} is already booked."
    elif seat_number not in all_seats:
        return f"Seat {seat_number} does not exist."
    booked_seats.append(seat_number)
    return f"Seat {seat_number} has been successfully booked!"

def get_available_seats():
    """
    Get a list of available seats by filtering out booked seats.
    
    Returns:
        list: List of available (unbooked) seats.
    """
    return [seat for seat in all_seats if seat not in booked_seats]
