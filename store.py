from products import Product

class Store:
    """
    Represents a store that manages a collection of Product objects.

    Provides functionality to add/remove products, calculate total stock,
    retrieve active products, and process customer orders.
    """

    def __init__(self, list_of_products:list[Product]):
        """
        Initialize the store with a list of products.

        Args:
            list_of_products (list): List of Product instances.
        """
        if not isinstance(list_of_products, list):
            raise TypeError("List of products should be list of Product")

        self.list_of_products = list_of_products


    def add_product(self, product:Product):
        """
        Add a product to the store inventory.

        Args:
            product (Product): The product to add.
        """
        if not isinstance(product, Product):
            raise TypeError("products must be a Product")

        self.list_of_products.append(product)


    def remove_product(self, product:Product):
        """
        Remove a product from the store inventory.

        Args:
            product (Product): The product to remove.

        Raises:
            ValueError: If the product is not in the list.
        """
        if not isinstance(product, Product):
            raise TypeError("products must be a Product")

        if product not in self.list_of_products:
            raise ValueError("Product not found")

        self.list_of_products.remove(product)


    def get_total_quantity(self):
        """
        Calculate the total quantity of all products in the store.

        Returns:
            int: Total quantity across all products.
        """
        total_quantity = 0

        for item in self.list_of_products:
            if not isinstance(item, Product):
                raise TypeError("Item must be Product")

            total_quantity += item.get_quantity()

        return total_quantity


    def get_all_products(self):
        """
        Retrieve all active products in the store.

        Returns:
            list[Product] | str: List of active products,
            or a message if no active products exist.
        """
        active_products = [item for item in self.list_of_products if
                           item.is_active() == True]

        if not active_products:
            return "There is no product in this store"

        return active_products


    def order(self, shopping_list) -> float:
        """
        Process a customer order.

        Each item in shopping_list should be a tuple:
        (Product, quantity)

        Args:
            shopping_list (list[tuple]): List of (Product, quantity) pairs.

        Returns:
            float: Total price of the order.
        """
        total_price = 0
        for item, quantity in shopping_list:
            total_price += item.buy(quantity)

        return float(total_price)
