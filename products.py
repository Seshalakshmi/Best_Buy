class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        try:
            if isinstance(new_name, str) and new_name != "":
                self._name = new_name
            else:
                raise ValueError("New name is Invalid")
        except TypeError:
            print("Name should be a string")
        except ValueError as e:
            print(e)

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        try:
            if isinstance(new_price, int) and new_price > 0:
                self._price = new_price
            else:
                raise ValueError("New price is Invalid")
        except TypeError:
            print("Price should be a integer")
        except ValueError as e:
            print(e)

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, new_quantity):
        try:
            if isinstance(new_quantity, int) and new_quantity > 0:
                self._quantity = new_quantity
            else:
                raise ValueError("New Quantity is Invalid")
        except TypeError:
            print("Quantity should be a integer")
        except ValueError as e:
            print(e)

    def is_active(self):
        if self._active:
            return Product.activate(self)
        else:
            return Product.deactivate(self)

    def activate(self):
        self._active = True
        return self._active

    def deactivate(self):
        self._active = False
        return self._active

    def show(self):
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}"

    def buy(self, quantity):
        try:
            if quantity <= self._quantity:
                self._quantity = self._quantity - quantity
                return float(self._price * quantity)
        except ValueError:
            print("Invalid quantity")


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()