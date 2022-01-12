class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0): 
    # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance

    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, balance):
        self.balance += balance
        return self

    def withdraw(self, balance):
        self.balance -= balance
        return self

    def display_account_info(self):
        print(f"Balance {self.balance}")
        return self

    def yield_interest(self):
        # if self.balance > 0:
        return self.balance + (self.balance * self.int_rate)

account1 = BankAccount(0.02, 10)
account2 = BankAccount(0.04, 1000)

account1.deposit(100)
account1.deposit(200)
account1.deposit(200)
account1.withdraw(150)
account1.display_account_info()
account1.yield_interest()

account2.deposit(1000).deposit(2000).withdraw(100).withdraw(200).withdraw(100).withdraw(100).display_account_info()
