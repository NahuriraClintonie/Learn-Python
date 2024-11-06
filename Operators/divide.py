def divide(a, b):
    """Returns the quotient of two numbers, or an error message if dividing by zero."""
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."
