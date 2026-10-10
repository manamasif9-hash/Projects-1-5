# shop.py


class InventoryItem:
    """
    Represents one item in the shop inventory.
    """

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_sold = 0

    def add_stock(self, quantity):
        """
        Add quantity to the current stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self.quantity += quantity

    def sell(self, quantity):
        """
        Sell a given quantity of the item.
        Returns the revenue from the sale.
        """
        if quantity <= 0:
            raise ValueError("Sale quantity must be greater than zero.")

        if quantity > self.quantity:
            raise ValueError(
                f"Not enough stock. Available stock: {self.quantity}"
            )

        self.quantity -= quantity
        self.total_sold += quantity

        revenue = self.price * quantity
        return revenue

    def __str__(self):
        return (
            f"{self.name} | "
            f"Price: Rs.{self.price:.2f} | "
            f"Stock: {self.quantity} | "
            f"Sold: {self.total_sold}"
        )


class Shop:
    """
    Manages all inventory items and sales.
    """

    def __init__(self, name):
        self.name = name
        self.items = {}
        self.sales = []

    def add_item(self, name, price, quantity):
        """
        Add a completely new item to the shop.
        """
        try:
            name = name.strip()

            if not name:
                raise ValueError("Item name cannot be empty.")

            if price <= 0:
                raise ValueError("Price must be greater than zero.")

            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")

            if name.lower() in [item.lower() for item in self.items]:
                raise ValueError(f"Item '{name}' already exists.")

            item = InventoryItem(name, price, quantity)
            self.items[name] = item

            return True

        except (ValueError, TypeError) as error:
            print(f"Error adding item: {error}")
            return False

    def add_stock(self, name, quantity):
        """
        Add stock to an existing item.
        """
        try:
            name = name.strip()

            if name not in self.items:
                raise KeyError(f"Item '{name}' does not exist.")

            if quantity <= 0:
                raise ValueError("Stock quantity must be greater than zero.")

            self.items[name].add_stock(quantity)

            print(
                f"Added {quantity} units of '{name}'. "
                f"New stock: {self.items[name].quantity}"
            )

            return True

        except (ValueError, TypeError, KeyError) as error:
            print(f"Error adding stock: {error}")
            return False

    def restock(self, name, quantity):
        """
        Restock an existing item.

        This is intentionally kept separate from add_stock so the
        project demonstrates both operations.
        """
        try:
            name = name.strip()

            if name not in self.items:
                raise KeyError(f"Cannot restock '{name}'. Item does not exist.")

            if quantity <= 0:
                raise ValueError("Restock quantity must be greater than zero.")

            self.items[name].add_stock(quantity)

            print(
                f"Restocked '{name}' with {quantity} units. "
                f"Current stock: {self.items[name].quantity}"
            )

            return True

        except (ValueError, TypeError, KeyError) as error:
            print(f"Restock error: {error}")
            return False

    def record_sale(self, name, quantity):
        """
        Record a sale and calculate revenue.
        """
        try:
            name = name.strip()

            if name not in self.items:
                raise KeyError(
                    f"Cannot sell '{name}'. Item does not exist."
                )

            if quantity <= 0:
                raise ValueError(
                    "Sale quantity must be greater than zero."
                )

            revenue = self.items[name].sell(quantity)

            sale = {
                "item": name,
                "quantity": quantity,
                "revenue": revenue
            }

            self.sales.append(sale)

            print(
                f"Sale successful: {quantity} x {name} "
                f"= Rs.{revenue:.2f}"
            )

            return revenue

        except (ValueError, TypeError, KeyError) as error:
            print(f"Sale error: {error}")
            return 0

    def get_total_revenue(self):
        """
        Calculate total revenue from all recorded sales.
        """
        return sum(sale["revenue"] for sale in self.sales)

    def get_total_items(self):
        """
        Return the number of different products.
        """
        return len(self.items)

    def display_inventory(self):
        """
        Display all inventory items.
        """
        if not self.items:
            print("\nInventory is empty.")
            return

        print("\n========== INVENTORY ==========")

        for item in self.items.values():
            print(item)

        print("===============================")

    def display_sales(self):
        """
        Display all recorded sales.
        """
        if not self.sales:
            print("\nNo sales have been recorded.")
            return

        print("\n========== SALES ==========")

        for sale in self.sales:
            print(
                f"{sale['item']} | "
                f"Quantity: {sale['quantity']} | "
                f"Revenue: Rs.{sale['revenue']:.2f}"
            )

        print("===========================")