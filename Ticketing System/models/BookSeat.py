# List to store the booked seats
booked_seats = []

def book_seat(seat_number):
    """
    Book a seat by adding it to the booked_seats list.
    
    Args:
        seat_number (str): The seat number to be booked.
    
    Returns:
        str: Success message if seat is booked, or failure if already booked.
    """
    # Check if the seat is already booked
    if seat_number in booked_seats:
        return f"Seat {seat_number} is already booked."
    
    # Book the seat
    booked_seats.append(seat_number)
    return f"Seat {seat_number} has been successfully booked! Book another seat please"
