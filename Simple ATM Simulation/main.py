# main.py

from account import Account
from transactions import deposit, withdraw

def atm_simulation():
    account = Account()  # Initialize account with default balance

    print("Welcome to Simple ATM Simulation!")

    while True:
        # Display the menu
        print("\n*** Main Menu ***")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        if choice == "1":
            # Check balance
            print(f"Your current balance is: ${account.check_balance()}")
        elif choice == "2":
            # Deposit money
            try:
                deposit_amount = float(input("Enter amount to deposit: $"))
                print(deposit(account, deposit_amount))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "3":
            # Withdraw money
            try:
                withdraw_amount = float(input("Enter amount to withdraw: $"))
                print(withdraw(account, withdraw_amount))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "4":
            # View transaction history
            history = account.get_transaction_history()
            if history:
                print("\n--- Transaction History ---")
                for i, transaction in enumerate(history, 1):
                    print(f"{i}. {transaction}")
            else:
                print("No transactions to display.")
        elif choice == "5":
            # Exit
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the simulation
if __name__ == "__main__":
    atm_simulation()
