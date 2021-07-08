class User():
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Blanace: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        print("Before the transfer, ", self.name, "'s balance is ", self.account_balance, "and ", other_user.name, "'s balance is ", other_user.account_balance)
        self.account_balance -= amount
        other_user.account_balance += amount
        print("After the transfer, the respective accounts stand at ", self.account_balance, " and ", other_user.account_balance)
        return self




guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
snape = User("Professor Snape", "snape@hogwarts.com")

guido.make_deposit(100).make_deposit(10000000).make_withdrawal(59468).display_user_balance()

monty.make_deposit(12).make_deposit(453156).make_withdrawal(1).make_withdrawal(7).display_user_balance()

snape.make_deposit(15000).make_withdrawal(1536).make_withdrawal(135).make_withdrawal(14).display_user_balance()

guido.transfer_money(snape, 1000000)



