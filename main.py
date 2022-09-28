class Wallet:
    def __init__(self, money):
        # money = 0
        self.money = money
        


    def credit(self, amount):
        self.money = amount + self.money
        print(f"you have money {self.money}")

    def debit(self, amount):
        self.money = self.money - amount
        print(f"you have money {self.money}")


wallet = Wallet(6)
# wallet = Wallet()  # This should default money inside the wallet to 0
print(wallet)
# print(wallet.money)
# wallet.credit(4)
# wallet.debit(5)


class Person:
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self. wallet = Wallet(money)
    


person = Person("Moh", 5, 50)
print(person.wallet.money)


# class Vendor:
#     # implement Vendor!
#     pass


# vendor = Vendor("Abdallah", 3, 6)


# class Customer:
#     # implement Customer!
#     pass


# customer = Customer("Abdallah", 3, 6)
