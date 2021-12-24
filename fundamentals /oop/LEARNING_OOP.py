# ---------------------------------------
# INSTANCE ATTRIBUTES

class User:
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

# Now we can create instances of the User :
User()
guido = User()
monty = User()
# Accessing the instance's attributes
print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

# We can also set the values for our instance's attributes:
guido.name = "Guido"
print(guido.name) # output: Guido
monty.name = "Monty"
print(monty.name) # output: Monty


# ---------------------------------------
# CLASS ATTRIBUTES

class User:
# declaring a class attribute
    bank_name = "First National Dojo"
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

# Changing Class Attributes on an instance:
guido = User()
monty = User()
guido.bank_name = "Dojo Credit Union"
print(guido.bank_name) # output: Dojo Credit Union
print(monty.bank_name) # output: First National Dojo

# Changing Class Attributes on an Entire Class:
User.bank_name = "Bank of Dojo"
print(guido.bank_name) # output: Bank of Dojo
print(monty.bank_name) # output: Bank of Dojo


# ----------------------------------------------------
# Let's adjust our code to allow arguments to be passed in upon instantiation:

class User:
    # class attributes get defined in the class
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
    	# we assign them accordingly
        self.name = name
        self.email = email_address
    	# the account balance is set to $0
        self.account_balance = 0
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

# -------------------------------------
# M E T H O D S
guido.make_deposit(100)

# To be able to call on this method, it needs to exist. Let's make it!

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
# NOW WE CAN CALL THE METHOD
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50

# CHECK USER.PY/answer AND CHAINING USER! GOO DSTUFF THERE.

# --------------------------------------------------------------
# This is how we write @classmethods:

class BankAccount:
    # class attribute
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum


# ---------------------------------------------------------------
# @STATCMETHOD

# If we wanted our BankAccount class to have a utility function to add or subtract we could implement @staticmethod on the class.

class BankAccount:
    # ... __init__ goes here
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
    	if (balance - amount) < 0:
	        return False
        else:
	        return True

# -------------------------------------------------------------

# Association Between Classes

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line

class User:
    def example_method(self):
    	# we can call the BankAccount instance's methods
        self.account.deposit(100)
    	# or access its attributes
    	print(self.account.balance)

# ------------------------------------------------------------------------------
#                                     FOUR PILLARS OF OOP

# 1  ENCAPSULATION:
class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")


# 2 INHERITANCE
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super.brew_now(beans)
        print("Frothy!!!")


#  3 POLYMORPHISM
class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super.brew_now(beans)
        print("Frothy!!!")
    def clean(self):
        print("Cleaning the froth!")



# 4 ABSTRACTION
class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def make_coffee(self):
        self.cafe.brew_now()


# -----------------------------------------------------------
#                                   INHERITANCE

# One way to make a distinction between account types would be to add an attribute of account_type to our BankAccount class. Then in each of our methods, we would have a series of conditional statements that would determine how the method would actually run. But this can get pretty clunky and hard to manage.

# If we go to the other extreme and just create two separate classes, we might end up with something like this:

# class CheckingAccount:
#     def __init__(self, int_rate, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#     def deposit(self, amount):
#     	# code
#     def withdraw(self, amount):
#     	# code
#     def write_check(self, amount):
#     	# code
#     def display_account_info(self):
#     	# code

# class RetirementAccount:
#     def __init__(self, int_rate, is_roth, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#     	self.is_roth = is_roth
#     def deposit(self, amount):
#     	# code - assess tax if necessary
#     def withdraw(self, amount):
#     	# code - assess penalty if necessary
#     def display_account_info(self):
#     	# code


# Still, this feels a little repetitive. Inheritance provides a balance between these two options--it allows us to have one parent class that holds the attributes and methods that are common between the new classes. In turn, each child class will only contain what is unique to that class:

class CheckingAccount(BankAccount):
    pass

class RetirementAccount(BankAccount):
    pass

# Would you believe that (assuming the BankAccount class is complete) with just the inclusion of the parent class in parentheses, both the CheckingAccount and RetirementAccount classes both have all the attributes and functionality of the parent class? Amazing! Now we just need to figure out how to add the differences, while maintaining what we need from the parent class.

# ----------------------------------------------------------------------

# Super
# Here's what we want our RetirementAccount __init__ method to do, and what our parent BankAccount class __init__ method does:
class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    	self.is_roth = is_roth

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

# parent class already does 2 of the 3 lines we're trying to execute in our RetirementAccount class? Let's utilize the parent's functionality for this method. To indicate we are trying to use the parent's methods, we call on it with the keyword super. From there, we can call on any of the parent's methods:

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
    	super().__init__(int_rate, balance)	
        self.is_roth = is_roth	

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance ="keyword operator from-rainbow">= balance

# The first line in our RetirementAccount __init__ method allows the parent to manage the setting of int_rate and balance. The only line we need to add is to set the is_roth attribute, since this is unique to the RetirementAccount class.

# Let's look at another example. Suppose we wanted to add some logic to our withdraw method.

class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
    	if is_early:
    	    amount = amount * 1.10
    	if (self.balance - amount) > 0:
    	    self.balance -= amount
        else:
    	    print("INSUFFICIENT FUNDS")
    	return self

class BankAccount:
    def withdraw(self, amount):
    	if (self.balance - amount) > 0:
    	    self.balance -= amount
        else:
    	    print("INSUFFICIENT FUNDS")
    	return self


# Hopefully you recognize the repetitiveness here and want to reduce it! So let's call on the parent to do the part of the code that is the same:

class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
    	if is_early:
    	    amount = amount * 1.10
    	super().withdraw(amount)
    	return self
    


class BankAccount:
    def withdraw(self, amount):
    	if (self.balance - amount) > 0:
    	    self.balance -= amount
        else:
    	    print("INSUFFICIENT FUNDS")
    	return self

# VOILA????

# --------------------------------------------------------------
# MODULES

# import the library
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)

# Creating Your Own Modules
# Writing your own Python modules is very simple. To create a module, we first create a new .py file with the module name in the same directory as the file that will import the module. Then we import it using the import command and the Python file name (without the .py extension)

# For example, let's create a module of arithmetic operations:

# modular_example/arithmetic.py

def add(x, y):
    return x + y
def multiply(x, y):
    return x * y
def subtract(x, y):
    return x - y



# modular_example/calculations.py

import arithmetic
print(arithmetic.add(5, 8))
print(arithmetic.subtract(10, 5))
print(arithmetic.multiply(12, 6))


# --------------------------------------------------------------
# Overriding
class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")
dad = Parent()
son = Child()
dad.method_a()
son.method_a() #notice this overrides the Parent method!


# invoking PARENT method_a!
# invoking CHILD method_a!


# --------------------------------------------------------------
#       Polymorphism

# We'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways
class Person:
    def pay_bill(self):
        raise NotImplementedError
# Millionaire inherits from Person
class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")

