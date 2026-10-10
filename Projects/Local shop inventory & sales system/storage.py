# storage.py

import os


INVENTORY_FILE = "inventory.txt"
SALES_FILE = "sales.txt"


def save_inventory(shop):
    """
    Save all inventory items to inventory.txt.

    Format:
    name|price|quantity|total_sold
    """

    try:
        with open(INVENTORY_FILE, "w", encoding="utf-8") as file:

            for item in shop.items.values():
                file.write(
                    f"{item.name}|"
                    f"{item.price}|"
                    f"{item.quantity}|"
                    f"{item.total_sold}\n"
                )

        return True

    except OSError as error:
        print(f"Could not save inventory: {error}")
        return False


def load_inventory(shop):
    """
    Load inventory from inventory.txt when the program starts.
    """

    if not os.path.exists(INVENTORY_FILE):
        return

    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:

            for line_number, line in enumerate(file, start=1):

                line = line.strip()

                if not line:
                    continue

                try:
                    parts = line.split("|")

                    if len(parts) != 4:
                        raise ValueError("Invalid inventory format.")

                    name = parts[0]
                    price = float(parts[1])
                    quantity = int(parts[2])
                    total_sold = int(parts[3])

                    item = shop.items.get(name)

                    if item is None:
                        shop.items[name] = __import__(
                            "shop"
                        ).InventoryItem(
                            name,
                            price,
                            quantity
                        )

                        shop.items[name].total_sold = total_sold

                except (ValueError, IndexError) as error:
                    print(
                        f"Skipping invalid inventory line "
                        f"{line_number}: {error}"
                    )

    except OSError as error:
        print(f"Could not load inventory: {error}")


def save_sale(sale):
    """
    Append one sale to sales.txt.

    Format:
    item|quantity|revenue
    """

    try:
        with open(SALES_FILE, "a", encoding="utf-8") as file:
            file.write(
                f"{sale['item']}|"
                f"{sale['quantity']}|"
                f"{sale['revenue']}\n"
            )

        return True

    except OSError as error:
        print(f"Could not save sale: {error}")
        return False


def load_sales(shop):
    """
    Reload sales history from sales.txt.
    """

    if not os.path.exists(SALES_FILE):
        return

    try:
        with open(SALES_FILE, "r", encoding="utf-8") as file:

            for line_number, line in enumerate(file, start=1):

                line = line.strip()

                if not line:
                    continue

                try:
                    parts = line.split("|")

                    if len(parts) != 3:
                        raise ValueError("Invalid sales format.")

                    item_name = parts[0]
                    quantity = int(parts[1])
                    revenue = float(parts[2])

                    sale = {
                        "item": item_name,
                        "quantity": quantity,
                        "revenue": revenue
                    }

                    shop.sales.append(sale)

                except (ValueError, IndexError) as error:
                    print(
                        f"Skipping invalid sales line "
                        f"{line_number}: {error}"
                    )

    except OSError as error:
        print(f"Could not load sales: {error}")


def load_all_data(shop):
    """
    Load inventory and sales when the application starts.
    """
    load_inventory(shop)
    load_sales(shop)