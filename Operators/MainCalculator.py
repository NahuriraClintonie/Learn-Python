import add
import subtract
import multiply
import divide
import modulus
import power
import floor_divide

def get_numbers():
    """Prompts the user to enter two numbers for the calculation."""
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a, b
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None, None

def main():
    print("Welcome to the Simple Python Calculator!")
    
    while True:
        # Display menu options
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Floor Division")
        print("8. Exit")
        
        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Thank you for using the calculator! Goodbye!")
            break

        # Get numbers from the user
        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
            continue

        # Perform operation based on user choice
        if choice == '1':
            result = add.add(num1, num2)
            print(f"The result of adding {num1} and {num2} is: {result}")
        elif choice == '2':
            result = subtract.subtract(num1, num2)
            print(f"The result of subtracting {num2} from {num1} is: {result}")
        elif choice == '3':
            result = multiply.multiply(num1, num2)
            print(f"The result of multiplying {num1} and {num2} is: {result}")
        elif choice == '4':
            result = divide.divide(num1, num2)
            print(f"The result of dividing {num1} by {num2} is: {result}")
        elif choice == '5':
            result = modulus.modulus(num1, num2)
            print(f"The result of modulus operation on {num1} and {num2} is: {result}")
        elif choice == '6':
            result = power.power(num1, num2)
            print(f"The result of {num1} raised to the power of {num2} is: {result}")
        elif choice == '7':
            result = floor_divide.floor_divide(num1, num2)
            print(f"The result of floor division of {num1} by {num2} is: {result}")
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
