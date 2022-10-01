from cgi import print_exception


class Wallet:
    def __init__(self, money):
        self.money = money
        
    def credit(self, amount):
        self.money += amount 
        # print(f"you have money {self.money}")

    def debit(self, amount):
        self.money -= amount
        # print(f"you have money {self.money}")


wallet = Wallet(6)
# wallet = Wallet()  # This should default money inside the wallet to 0
# print(wallet)
# print(wallet.money)
# wallet.credit(4)
# wallet.debit(5)


class Person:
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.wallet = Wallet(money)
    
    def moveTo(self, point):
        self.location = point


person = Person("Moh", 5, 50)
print(person.wallet.money)


class Vendor(Person):
    def __init__(self, name, location, money):
        super().__init__(name, location, money)
        self.range = 5
        self.price = 1

    def sellTo(self, customer, number_of_icecreams):
        self.location = customer.location
        self.wallet.credit(number_of_icecreams * self.price)
        customer.wallet.debit(number_of_icecreams * self.price)


vendor = Vendor("Abdallah", 3, 6)
# print(vendor)

class Customer(Person):
    def __init__(self, name, location, money):
        super().__init__(name, location, money)

    def _is_in_range(self, vendor):
        distance = vendor.location - self.location
        if distance > vendor.range:
            return True
        else:
            return False

    def _have_enough_money(self, vendor, number_of_icecreams):
        if self.wallet.money >= vendor.price * number_of_icecreams:
            return True
        else:
            return False

    def request_icecream(self, vendor, number_of_icecreams):
        if self._is_in_range(vendor) and self._have_enough_money(
            vendor, number_of_icecreams):
            vendor.sellTo(self, number_of_icecreams)


customer = Customer("Abdallah", 3, 6)