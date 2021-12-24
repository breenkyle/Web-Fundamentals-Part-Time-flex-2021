# INSTRUCTOR ANSWER FROM PREVIOUS ASSINGMENT REWORKED AND IT WORKED AS THE EXAMPLE SHOWED
class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawl(self,amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


kyle = User("Kyle Breen")
montgomery = User("Mongomery Burns")
victoria = User("Victoria von Katze")

# adrien.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawl(45)
# adrien.display_user_balance()

kyle.make_deposit(505).make_deposit(272).make_deposit(33).make_withdrawl(33)
kyle.display_user_balance()
montgomery.make_deposit(1000).make_deposit(1000).make_withdrawl(500).make_withdrawl(500)
montgomery.display_user_balance()
victoria.make_deposit(1000).make_withdrawl(111).make_withdrawl(111).make_withdrawl(112)
victoria.display_user_balance()
kyle.transfer_money(77, victoria)


# -----------------------------------------------------------------------------------

# class User:
#     def __init__(self, name, email, account_balance):
#         self.name = name
#         self.email = email
#         self.account_balance = 0
#     def make_deposit(self, amount):
#     	self.account_balance += amount
        # return self       THIS DID NOT WORK :( - REWORKED ANSWER FROM LAST ASSIGNMENT ABOVE
#     def make_withdrawl(self, amount):
#         self.account_balance -= amount
#     def display_user_balance(self):
#         self.account_balance
#         # def display_user_balance(self):
#         # print(f"User: {self.name}, Balance: {self.amount}")
#     def transfer_money(self, other_user, amount):
#         self.make_withdrawl(amount)
#         other_user.make_deposit(amount)

# kyle = User("Kyle Breen", "kyle@python.com", 777)
# montgomery = User("Montgomery Burns", "montgomery@python.com", 1000)
# victoria = User("Victoria von Katze", "victoria@python.com", 666)


# kyle.make_deposit(505)
# kyle.make_deposit(272)
# kyle.make_deposit(33)
# kyle.make_withdrawl(33)
# print(kyle.account_balance)
# montgomery.make_deposit(1000)
# montgomery.make_deposit(1000)
# montgomery.make_withdrawl(500)
# montgomery.make_withdrawl(500)
# print(montgomery.account_balance)
# victoria.make_deposit(1000)
# victoria.make_withdrawl(111)
# victoria.make_withdrawl(111)
# victoria.make_withdrawl(112)
# print(victoria.account_balance)
# kyle.transfer_money(victoria, 77)
# print(kyle.account_balance)
# print(victoria.account_balance)