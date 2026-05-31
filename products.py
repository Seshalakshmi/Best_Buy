from typing import Union

class Product:
    """
    Represents a product available for purchase.

    A product has a name, unit price, available quantity, and an active
    status indicating whether it can be purchased. The class provides
    functionality for inventory management, product activation/deactivation,
    and purchase processing.
    """
    def __init__(self, name:str, price:Union[float, int], quantity:int):
        """
        Initialize a Product instance.

        Args:
            name: Product name.
            price: Unit price of the product.
            quantity: Initial stock quantity.

        Raises:
            TypeError: If any argument has an invalid type.
            ValueError: If name is empty, or if price/quantity are negative.
        """
        if not isinstance(name, str):
            raise TypeError("Name should be string")

        if not isinstance(price, (float, int)):
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
        """
        Return the current available stock quantity.

        Returns:
            int: Number of units currently available.
        """
        return self._quantity

    def set_quantity(self, new_quantity:int):
        """
        Reduce the available stock by the specified quantity.

        If the resulting quantity reaches zero, the product is automatically
        deactivated.

        Args:
            new_quantity: Number of units to remove from stock.

        Raises:
            TypeError: If `new_quantity` is not an integer.
            ValueError: If `new_quantity` is negative or exceeds available stock.
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
        Determine whether the product is currently active.

        Returns:
            bool: True if the product is active; otherwise False.
        """
        return self._active

    def activate(self):
        """
        Mark the product as active and available for purchase.
        """
        self._active = True


    def deactivate(self):
        """
        Mark the product as inactive and unavailable for purchase.
        """
        self._active = False


    def show(self):
        """
        Return a human-readable representation of the product.

        Returns:
            str: Formatted product details including name, price, and quantity.
        """
        return (f"{self._name}, Price: {self._price}, Quantity: "
                f"{self._quantity}")

    def buy(self, quantity:int):
        """
        Purchase a specified quantity of the product.

        The requested quantity is deducted from inventory and the total
        purchase price is returned.

        Args:
            quantity: Number of units to purchase.

        Returns:
            float: Total cost of the purchase.

        Raises:
            ValueError: If the product is inactive or if the purchase quantity
                is invalid.
        """
        if self._active:
            self.set_quantity(quantity)
            return float(self._price * quantity)

        else:
            raise ValueError("This product is inactive")
