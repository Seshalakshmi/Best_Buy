from products import Product
from store import Store

"""
Command-line interface for the store management application.

This module provides the user-facing functionality for interacting
with the store, including viewing available products, checking
inventory levels, placing orders, and exiting the application.
"""

def list_of_products_in_store(store_items: Store) -> None:
    """
    Display all active products available in the store inventory.

    Retrieves the list of active products from the provided store and
    prints each product with a numbered index and its details.

    Args:
        store_items: The store instance containing the product inventory.
    """
    all_products = store_items.get_all_products()
    if not all_products:
        print("No products available.")
        return

    for nos, item in enumerate(all_products, 1):
        print(f"{nos}: {Product.show(item)}")
    print("________")


def total_stock_quantity(store_items: Store) -> None:
    """
    Display the total quantity of products currently available in the store.

    Args:
        store_items: The store instance whose inventory quantity is
            calculated and displayed.
    """
    if not store_items:
        print("No products available.")
        return

    print(f"Total of {store_items.get_total_quantity()} items in store")


def make_order(store_items: Store) -> None:
    """
    Interactively create and process a customer order.

    Prompts the user to select products and specify purchase quantities.
    Selected items are collected into an order and submitted to the store
    for processing. Upon successful completion, the total payment amount
    is displayed.

    Args:
        store_items: The store instance used to retrieve products and
            process customer purchases.

    Raises:
        ValueError: Propagated if an invalid order is submitted.
        TypeError: Propagated if invalid order data is encountered.
    """
    all_products = store_items.get_all_products()
    if not all_products:
        print("No products available.")
        return

    list_of_products_in_store(store_items)
    print("When you want to finish order, enter empty text. ")
    purchased = []
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
            shopping = int(shopping) - 1
            purchase_quantity = int(purchase_quantity)

        except ValueError:
            print("Error adding product!")
            continue

        if shopping < 0 or shopping >= len(all_products):
            print("Error: Invalid product number!")
            continue

        item = all_products[shopping]

        if purchase_quantity <= 0:
            print("Error: Quantity must be greater than zero.")
            continue

        purchased.append((item, purchase_quantity))
        print("Product added to list!")

    if purchased:
        try:
            total_payment = store_items.order(purchased)
            print("*********")
            print(f"Order made! Total payment: ${total_payment:.2f}")
        except (TypeError, ValueError) as e:
            print(f"Order execution failed: {e}")
    else:
        print("No items ordered.")


def exit_program() -> None:
    """
    Display a farewell message and terminate the application.
    """
    print("GoodBye!")


def start(store_items: Store) -> None:
    """
    Launch the interactive store menu.

    Displays available menu options, processes user selections,
    and continues execution until the user chooses to exit the
    application.

    Args:
        store_items: The store instance used to perform inventory
            and ordering operations.
    """
    while True:
        print("\n\tStore Menu")
        print("\t__________")
        print("1. List all products in store\n"
              "2. Show total amount in store\n"
              "3. Make an order\n"
              "4. Quit")

        options = {
            1: list_of_products_in_store,
            2: total_stock_quantity,
            3: make_order
        }

        user_input = input("Please choose a number: ")
        if not user_input.isdigit():
            print("Please provide a valid number")
            continue

        user_input = int(user_input)

        if user_input == 4:
            exit_program()
            break

        action = options.get(user_input)

        if action:
            action(store_items)
        else:
            print("Invalid option")


def main() -> None:
    """
    Initialize and run the store application.

    Creates the initial product inventory, instantiates the store,
    and starts the command-line interface.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
