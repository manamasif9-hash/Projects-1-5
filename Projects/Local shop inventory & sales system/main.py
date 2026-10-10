# main.py

from shop import Shop
from storage import (
    load_all_data,
    save_inventory,
    save_sale
)
from reports import (
    generate_daily_summary,
    generate_detailed_report
)


def get_integer(prompt):
    """
    Safely get an integer from the user.
    """

    while True:
        try:
            value = int(input(prompt))
            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_float(prompt):
    """
    Safely get a floating-point number from the user.
    """

    while True:
        try:
            value = float(input(prompt))
            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def add_new_item(shop):
    """
    Ask the user for information and add a new item.
    """

    print("\n========== ADD NEW ITEM ==========")

    name = input("Enter item name: ").strip()

    price = get_float("Enter item price (Rs.): ")
    quantity = get_integer("Enter initial quantity: ")

    success = shop.add_item(
        name,
        price,
        quantity
    )

    if success:
        save_inventory(shop)
        print("Item added successfully.")


def add_stock_menu(shop):
    """
    Add stock using the add_stock method.
    """

    print("\n========== ADD STOCK ==========")

    name = input("Enter item name: ").strip()
    quantity = get_integer("Enter quantity to add: ")

    if shop.add_stock(name, quantity):
        save_inventory(shop)


def restock_menu(shop):
    """
    Restock an item.
    """

    print("\n========== RESTOCK ==========")

    name = input("Enter item name: ").strip()
    quantity = get_integer("Enter restock quantity: ")

    if shop.restock(name, quantity):
        save_inventory(shop)


def record_sale_menu(shop):
    """
    Record a customer sale.
    """

    print("\n========== RECORD SALE ==========")

    name = input("Enter item name: ").strip()
    quantity = get_integer("Enter quantity sold: ")

    revenue = shop.record_sale(
        name,
        quantity
    )

    if revenue > 0:

        # Find the latest sale
        latest_sale = shop.sales[-1]

        # Save the sale to sales.txt
        save_sale(latest_sale)

        # Save updated stock
        save_inventory(shop)


def inventory_menu(shop):
    """
    Display inventory.
    """
    shop.display_inventory()


def sales_menu(shop):
    """
    Display sales.
    """
    shop.display_sales()


def summary_menu(shop):
    """
    Display daily summary.
    """

    threshold = get_integer(
        "Enter low-stock threshold (e.g. 5): "
    )

    if threshold < 0:
        print("Threshold cannot be negative.")
        return

    generate_daily_summary(
        shop,
        threshold
    )


def show_menu():
    """
    Display the main menu.
    """

    print("\n")
    print("==========================================")
    print("       LOCAL SHOP INVENTORY SYSTEM")
    print("==========================================")
    print("1. Add new item")
    print("2. Add stock")
    print("3. Restock item")
    print("4. Record sale")
    print("5. View inventory")
    print("6. View sales")
    print("7. Daily summary")
    print("8. Detailed report")
    print("9. Save data")
    print("0. Exit")
    print("==========================================")


def main():
    """
    Main application function.
    """

    shop = Shop("My Local Shop")

    # Load previous data when application starts
    load_all_data(shop)

    print("\nWelcome to the Local Shop Inventory System!")

    if shop.items:
        print(
            f"Loaded {len(shop.items)} "
            f"inventory item(s)."
        )

    if shop.sales:
        print(
            f"Loaded {len(shop.sales)} "
            f"previous sale(s)."
        )

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":
            add_new_item(shop)

        elif choice == "2":
            add_stock_menu(shop)

        elif choice == "3":
            restock_menu(shop)

        elif choice == "4":
            record_sale_menu(shop)

        elif choice == "5":
            inventory_menu(shop)

        elif choice == "6":
            sales_menu(shop)

        elif choice == "7":
            summary_menu(shop)

        elif choice == "8":
            generate_detailed_report(shop)

        elif choice == "9":
            save_inventory(shop)
            print("Inventory saved successfully.")

        elif choice == "0":
            save_inventory(shop)
            print("\nData saved.")
            print("Thank you for using the system!")
            break

        else:
            print(
                "Invalid menu choice. "
                "Please select a number from 0 to 9."
            )


if __name__ == "__main__":
    main()