# For this assignment, we'll add some functionality to the User class:
# 1)  make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# 2)  display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

# Create a file with the User class, including the __init__ and make_deposit methods
# Add a make_withdrawal method to the User class
# Add a display_user_balance method to the User class
# Create 3 instances of the User class
# Have the first user make 3 deposits and 1 withdrawal and then display their balance
# Have the second user make 2 deposits and 2 withdrawals and then display their balance
# Have the third user make 1 deposits and 3 withdrawals and then display their balance
# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

class User:
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
    	self.account_balance += amount
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        self.account_balance
        # def display_user_balance(self):
        # print(f"User: {self.name}, Balance: {self.amount}")
    def transfer_money(self, other_user, amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)

kyle = User("Kyle Breen", "kyle@python.com", 777)
montgomery = User("Montgomery Burns", "montgomery@python.com", 1000)
victoria = User("Victoria von Katze", "victoria@python.com", 666)


kyle.make_deposit(505)
kyle.make_deposit(272)
kyle.make_deposit(33)
kyle.make_withdrawl(33)
print(kyle.account_balance)
montgomery.make_deposit(1000)
montgomery.make_deposit(1000)
montgomery.make_withdrawl(500)
montgomery.make_withdrawl(500)
print(montgomery.account_balance)
victoria.make_deposit(1000)
victoria.make_withdrawl(111)
victoria.make_withdrawl(111)
victoria.make_withdrawl(112)
print(victoria.account_balance)
kyle.transfer_money(victoria, 77)
print(kyle.account_balance)
print(victoria.account_balance)
