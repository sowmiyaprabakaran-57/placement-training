#Scenario:
#You are creating a banking system. Each customer has a name, account number, and balance.
#Implement a function to transfer money from one account to another.

#Code:
class Customer:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

def transfer_money(sender, receiver, amount):
    if sender.balance >= amount:
        sender.balance -= amount
        receiver.balance += amount
    else:
        print("Insufficient funds")

alice = Customer("Alice", "12345", 1000)
bob = Customer("Bob", "67890", 500)
transfer_money(alice, bob, 200)
print(alice.balance)  # Output: 800
print(bob.balance)    # Output: 700
