import products
import store


def start(store_items):
    while True:
        print("\n\tStore Menu")
        print("\t__________")
        print("1. List all products in store\n"
              "2. Show total amount in store\n"
              "3. Make an order\n"
              "4. Quit")

        user_input = int(input("Please choose a number: "))
        if user_input == 1:
            all_products = store_items.get_all_products()
            for nos, item in enumerate(all_products, 1):
                print(
                    f"{nos}: {products.Product.get_name(item)}, Price: "
                    f"{products.Product.get_price(item)}, Quantity: "
                    f"{products.Product.get_quantity(item)}")
            print("________")

        elif user_input == 2:
            print(
                f"Total of {store_items.get_total_quantity()} items in store")

        elif user_input == 3:
            all_products = store_items.get_all_products()
            for nos, item in enumerate(all_products, 1):
                print(
                    f"{nos}: {products.Product.get_name(item)}, Price: "
                    f"{products.Product.get_price(item)}, Quantity: "
                    f"{products.Product.get_quantity(item)}")
            print("________")

            print("When you want to finish order, enter empty text. ")
            total_amount = 0
            while True:
                shopping = input("Which product # do you want? ")
                if shopping == "":
                    print("Thank You. Welcome!")
                    break

                purchase_quantity = input("What amount do you want? ")
                if purchase_quantity == "":
                    print("Error while making order!")
                    continue

                try:
                    shopping = int(shopping)
                    purchase_quantity = int(purchase_quantity)

                except ValueError:
                    print("Error adding product!")
                    continue
                purchased = []
                for nos, item in enumerate(all_products, 1):
                    if (int(shopping) == nos and int(
                            purchase_quantity) <=
                            products.Product.get_quantity(
                            item)):
                        purchased.append((item, int(purchase_quantity)))

                if purchased:
                    total_amount += store_items.order(purchased)
                    print("Product added to list!")

            if total_amount > 0:
                print("*********")
                print(f"Order made! Total payment: ${total_amount}")
            else:
                print(
                    "Error while making order! Quantity larger than what "
                    "exists")

        elif user_input == 4:
            print("GoodBye!")
            break

        else:
            print("Error with your choice! Try again!")


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
        ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
