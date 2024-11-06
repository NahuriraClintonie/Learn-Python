def floor_divide(a, b):
    """Returns the floor division result of two numbers, or an error message if dividing by zero."""
    if b != 0:
        return a // b
    else:
        return "Error: Cannot perform floor division by zero."
