'''Stores the class of wallets'''

class Wallet:
    '''Wallet stores balance'''

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            return "Insufficient Funds"

        self.balance = self.balance - amount
        return f"Remaining Balance: ${self.balance}"

    def add_Cash(self, amount):
        self.balance += amount

    def __repr__(self):
        return f"Wallet with a balance of: ${self.balance}"
