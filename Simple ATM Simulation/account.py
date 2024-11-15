
class Account:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)

    def get_transaction_history(self):
        return self.transaction_history[-5:]  # Last 5 transactions
