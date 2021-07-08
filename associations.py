class BankAccount:
    all_accounts = []
    def __init__(self, acct_name, int_rate = 0.02, balance = 0):
        self.acct_name = acct_name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
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
            print(account.balance, account.int_rate)


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def make_deposit(self, acct_name, amount):
        for i in self.accounts:
            if i.acct_name == acct_name:
                i.deposit(amount)
        return self

    def make_withdrawal(self, acct_name, amount):
        for i  in self.accounts:
            if i.acct_name == acct_name:
                i.deposite(amount)
        return self

    def display_account_balance(self, name):
        for i in self.accounts:
            if i.name == name:
                print(f"Account: {i.name}, Balance: {i.balance}")
        return self

    def transfer_money(self, payer_acct_name, other_user, receiver_acct_name, amount):
        for i in self.accounts:
            if i.acct_name == payer_acct_name:
                for j in other_user.accounts:
                    if j.acct_name == receiver_acct_name:
                        print("Before the transfer, the balance of ", self.name, "'s ", i.acct_name, "account was:", i.balance)
                        print("Before the transfer, the balance of ", other_user.name, "'s ", j.acct_name, "account was:", j.balance)
                        i.withdraw(amount)
                        j.deposit(amount)
                        print("After the transfer, the balance of ", self.name, "'s ", i.acct_name, "account is now:", i.balance)
                        print("After the transfer, the balance of ", other_user.name, "'s ", j.acct_name, "account is now:", j.balance)
        return self

    def create_account(self, name):
        self.accounts.append(BankAccount(name))
        return self

    def show_user_account_info(self, action):
        if action == "balance":
            for i in self.accounts:
                print(i.balance)
        if action == "name":
            for i in self.accounts:
                print(i.name)
        if action == "int_rate":
            for i in self.accounts:
                print(i.int_rate)

    @classmethod
    def display_number_of_accounts(cls):
        for accountnumber in cls.number_of_accounts:
            print(accountnumber)

david = User("David Storer", "dstorer2@gmail.com")

steve = User("Steve Erwin", "steve@croikie.com")

david.create_account("checking").create_account("savings")
steve.create_account("checking")

david.make_deposit("savings", 1000000).transfer_money("savings", steve, "checking", 499999)


