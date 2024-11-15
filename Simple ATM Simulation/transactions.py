def deposit(account, amount):
    if amount > 0:
        account.balance += amount
        account.add_transaction(f"Deposited ${amount}")
        return f"Successfully deposited ${amount}."
    return "Amount must be greater than 0."

def withdraw(account, amount):
    if amount > 0:
        if amount <= account.balance:
            account.balance -= amount
            account.add_transaction(f"Withdrew ${amount}")
            return f"Successfully withdrew ${amount}."
        return "Insufficient funds."
    return "Amount must be greater than 0."
