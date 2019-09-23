class Bank:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
        self.customers=[]

    def add_customer(self, customer_name):
        self.customers.append(customer_name)
        print("{} Bank has new customer {}".format(self.name,customer_name.name))


class Customer:

    def __init__(self, name):
        self.name = name
        self.account = Account(balance=0)


class Account:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Funds!")
            return
        self.balance = self.balance - amount
        # print(self.balance)

    def get_balance(self):
        return self.balance



axis_bank=Bank("Axis","BLR")
vishal_sobani = Customer("Vishal Sobani")
axis_bank.add_customer(vishal_sobani)
print(vishal_sobani.account.get_balance())
vishal_sobani.account.deposit(1000)
vishal_sobani.account.withdraw(99)
print(vishal_sobani.account.get_balance())

hdfc_bank=Bank("HDFC", "BLR")
tarzan_skills=Customer("tarzan_skills")
hdfc_bank.add_customer(tarzan_skills)
tarzan_skills.account.deposit(20020)
tarzan_skills.account.withdraw(200)
print(tarzan_skills.account.get_balance())


