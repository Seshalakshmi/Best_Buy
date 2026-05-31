from typing import Union

class Product:
    """
        Represents a product with a name, price, quantity, and active status.

        Provides methods to get and set attributes, activate/deactivate the product,
        display product information, and process purchases.
    """
    def __init__(self, name:str, price:Union[float, int], quantity:int):
        """
                Initialize a new Product instance.

                Args:
                    name (str): The name of the product.
                    price (int | float): The price per unit of the product.
                    quantity (int): The available stock quantity.
        """
        if not isinstance(name, str):
            raise TypeError("Name should be string")

        if not isinstance(price, Union[float, int]):
            raise TypeError("Price should be a float or integer")

        if not isinstance(quantity, int):
            raise TypeError("Quantity should be an integer")

        if not name:
            raise ValueError("Name is required")

        if not price or price < 0:
            raise ValueError("Price is required")

        if not quantity or quantity < 0:
            raise ValueError("Quantity is required")

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True


    def get_quantity(self) -> int:
        """Return the available quantity of the product."""
        return self._quantity

    def set_quantity(self, new_quantity:int):
        """
                Set a new quantity for the product.

                Args:
                    new_quantity (int): The updated stock quantity (must be positive).

                Raises:
                    ValueError: If quantity is not a positive integer.
                    TypeError: If type is invalid.
        """
        if not isinstance(new_quantity, int) and new_quantity > 0:
            raise TypeError("Quantity is Invalid")

        if new_quantity > self._quantity:
            raise ValueError("Quantity is out of stock")

        if new_quantity < 0:
            raise ValueError("Please type a positive number")

        self._quantity -= new_quantity

        if self._quantity == 0:
            self.deactivate()


    def is_active(self):
        """
            Check whether the product is active.

            Returns:
                bool: True if active, False otherwise.
        """
        return self._active

    def activate(self):
        """
            Activate the product.

            Returns:
                bool: True after activation.
        """
        self._active = True


    def deactivate(self):
        """
        Deactivate the product.

        Returns:
            bool: False after deactivation.
        """
        self._active = False


    def show(self):
        """
                Return a formatted string describing the product.

                Returns:
                    str: Product details.
        """
        return (f"{self._name}, Price: {self._price}, Quantity: "
                f"{self._quantity}")

    def buy(self, quantity:int):
        """
            Purchase a given quantity of the product.

            Reduces stock if enough quantity is available.

            Args:
                quantity (int): Number of items to purchase.

            Returns:
                float: Total price for the purchase.

            Raises:
                ValueError: If purchase is invalid or insufficient stock.
        """
        if self._active:
            self.set_quantity(quantity)
            return float(self._price * quantity)

        else:
            raise ValueError("This product is inactive")
