# Define the user class
class User:
    def __init__(self,user_id, name, phone):
        self.user_id = user_id  #Initialize user id
        self.name = name  #Initialize user name
        self.phone = phone  #initialize user phone number
        self.account=Account(self)  #Creating account for user
    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.phone})"  #representation of the user object


# Define account class
class Account:
        def __init__(self,user):
            self.user = user
            self.balance = 0.0

        def deposit(self,amount):
            if amount > 0:   #Check if the deposit is > 0
                self.balance += amount
                print(f"{amount} deposited. New balance: {self.balance}")
            else:
                print("Deposited Amount must be greater than 0 / positive")

        def withdraw(self,amount):
            if 0<amount<=self.balance:
                self.balance -= amount
                print(f"{amount} withdrawn. New balance: {self.balance}")
            else:
                print("Insufficient funds or invalid amount")

        def __repr__(self):
            return f"Account(User: {self.user.name}, Balance: {self.balance})"  #Representation of account object


# Define transaction class
class Transaction:
    def __init__(self,account,amount,transaction_type):
            self.account = account
            self.amount = amount
            self.transaction_type = transaction_type

    def process(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type")
    def __repr__(self):
        return f"Transaction(Account{self.account}, Amount : {self.amount}, Type : {self.transaction_type})"


# example usage // object
user1=User(101,"Abigael Margaret",734091820)
print(user1)

# Deposit amount
user1.account.deposit(1000)

user1.account.withdraw(500)

transaction1=Transaction(user1.account,200,"deposit")
transaction1.process()

transaction2=Transaction(user1.account,100,"withdraw")
transaction2.process()

print(user1.account)

# example2
user2=User(102,"Kylie Rains",757842015)
print(user2)
user2.account.deposit(5000)
user2.account.withdraw(1000)

transaction3=Transaction(user2.account,800,"deposit")
transaction3.process()

transaction4=Transaction(user2.account,600,"withdraw")
transaction4.process()

print(user2.account)