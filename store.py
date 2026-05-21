import products

class Store:

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0

        for items in self.list_of_products:
            total_quantity += items.get_quantity()

        return total_quantity

    def get_all_products(self):
        active_products = []

        for items in self.list_of_products:
            if items.is_active():
                active_products.append(items)
            else:
                return f"There is no product in this store"
        return active_products


    def order(self, shopping_list):
        total_price = 0
        for items, quantity in shopping_list:
            total_price += items.buy(quantity)

        return f"Order cost: {total_price} dollars."



product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))