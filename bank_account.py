class Bank_Account:
    all_accounts = []
    def __init__(self, interest_rate, balance = 0):
        self.interest_rate = interest_rate
        self.balance = balance
        Bank_Account.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_balance(self):
        print("Balance: $", self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.interest_rate
        else:
            False
        return self
    @classmethod
    def display_account_info(cls):
        for account in cls.all_accounts:
            print(account.balance, account.interest_rate)

account1 = Bank_Account(.05, 100000)
account2 = Bank_Account(.02)

# account1.deposit(300).deposit(700).deposit(5000).withdraw(31000).yield_interest().display_account_balance()

# account2.deposit(500000).deposit(100000).withdraw(140003).withdraw(153435).withdraw(105).withdraw(35135).yield_interest().display_account_balance()

Bank_Account.display_account_info()