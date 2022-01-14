class BankAccount:
    accounts = []
    #set default variables for int_rate and balance
    def __init__(self, int_rate = 0.01, balance = 0): 
    # your code here-setting instance attributes
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    # create deposit function
    def deposit(self, amount):
        self.balance += amount
        return self

    # create withdraw function with conditional in event no funds available
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            #if funds below 0 will print insufficient funds and chrg fee statement
            print("Insufficient Funds: Chargin a $5 fee")
            # deduct $5 fee from account
            self.balance -= 5
        return self 

    # create display account info function with string
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    # crate interest yeild function
    def yield_interest(self):
        if(self.balance) > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    """create class method to display all accoutns
    note: class methods have no access to the instance attribute
    or any attribute that starts with self."""
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

account1 = BankAccount(0.02, 10)
account2 = BankAccount(0.04, 1000)

account1.deposit(100).deposit(200).deposit(200).withdraw(150).yield_interest().display_account_info()

account2.deposit(1000).deposit(2000).withdraw(100).withdraw(200).withdraw(100).withdraw(100).yield_interest().display_account_info()

BankAccount.print_all_accounts()