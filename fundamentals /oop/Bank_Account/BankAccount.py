# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

class BankAccount:
    bank_name = "First National Dojo"    #uneeded
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.amount = 0             #not needed...
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.amount += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds, Charging a $5 fee")
            self.balance - 5.00
        return self
    @staticmethod
    def can_withdraw(balance,amount):      #more complicated than it should have been. 
        if (balance - amount) < 0:
            return False
        else:
            return True
    def display_account_info(self):
        print(f"BankAccount: {self.int_rate}, Balance: {self.amount}")
    def yield_interest(self):
        if self.balance > 0:
	        self.balance + .05   #CHECK BELOW
        else:
            return "Not Intersesting"
        return self
        # I think I am missing something to make yield_interest work...
        #                          \/THIS 
         #    self.balance += (self.balance * self.int_rate)

    @classmethod
    def all_balances(cls):
        sum = 0 
        for account in cls.all_accounts:
            sum += account.balance
        return sum 
    # this didn't work/show anything?

acct1 = BankAccount(.05, 10000)
acct2 = BankAccount(.05, 5000)

acct1.deposit(10000).deposit(300).deposit(2500).withdraw(700).yield_interest().display_account_info()

acct2.deposit(5000).deposit(5000).withdraw(1250).withdraw(1250).withdraw(1250).withdraw(1250).yield_interest()
acct2.display_account_info()