class Product:
    """
        Represents a product with a name, price, quantity, and active status.

        Provides methods to get and set attributes, activate/deactivate the product,
        display product information, and process purchases.
    """
    def __init__(self, name, price, quantity):
        """
                Initialize a new Product instance.

                Args:
                    name (str): The name of the product.
                    price (int | float): The price per unit of the product.
                    quantity (int): The available stock quantity.
        """
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True

    def get_name(self):
        """Return the name of the product."""
        return self._name

    def set_name(self, new_name):
        """
                Set a new name for the product.

                Args:
                    new_name (str): The new product name.

                Raises:
                    ValueError: If new_name is empty or not a string.
                    TypeError: If type is invalid.
        """
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
        """Return the price of the product."""
        return self._price

    def set_price(self, new_price):
        """
                Set a new price for the product.

                Args:
                    new_price (int): The new price value (must be positive integer).

                Raises:
                    ValueError: If price is not a positive integer.
                    TypeError: If type is invalid.
        """
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
        """Return the available quantity of the product."""
        return self._quantity

    def set_quantity(self, new_quantity):
        """
                Set a new quantity for the product.

                Args:
                    new_quantity (int): The updated stock quantity (must be positive).

                Raises:
                    ValueError: If quantity is not a positive integer.
                    TypeError: If type is invalid.
        """
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
        """
            Check whether the product is active.

            Returns:
                bool: True if active, False otherwise.
        """
        if self._active:
            return Product.activate(self)
        return Product.deactivate(self)

    def activate(self):
        """
            Activate the product.

            Returns:
                bool: True after activation.
        """
        self._active = True
        return self._active

    def deactivate(self):
        """
        Deactivate the product.

        Returns:
            bool: False after deactivation.
        """
        self._active = False
        return self._active

    def show(self):
        """
                Return a formatted string describing the product.

                Returns:
                    str: Product details.
        """
        return (f"{self._name}, Price: {self._price}, Quantity: "
                f"{self._quantity}")

    def buy(self, quantity):
        """
                Purchase a given quantity of the product.

                Reduces stock if enough quantity is available.

                Args:
                    quantity (int): Number of items to purchase.

                Returns:
                    float: Total price for the purchase.
                    None: If purchase is invalid or insufficient stock.
        """
        try:
            if quantity <= self._quantity:
                self._quantity = self._quantity - quantity
                return float(self._price * quantity)
        except ValueError:
            print("Invalid quantity")
