class Store:

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0

        for item in self.list_of_products:
            total_quantity += item.get_quantity()

        return total_quantity

    def get_all_products(self):
        active_products = []

        for item in self.list_of_products:
            if item.is_active():
                active_products.append(item)

        if not active_products:
            return f"There is no product in this store"

        return active_products

    def order(self, shopping_list):
        total_price = 0
        for item, quantity in shopping_list:
            total_price += item.buy(quantity)

        return total_price
