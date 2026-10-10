# reports.py


def generate_daily_summary(shop, low_stock_threshold=5):
    """
    Generate a daily shop summary.

    Uses list and dictionary comprehensions.
    """

    print("\n========== DAILY SUMMARY ==========")

    # Edge case: empty inventory
    if not shop.items:
        print("Inventory is empty.")
        print("Total Revenue: Rs.0.00")
        print("Top-selling item: No sales")
        print("Low-stock items: None")
        print("===================================")
        return

    # Total revenue
    total_revenue = sum(
        sale["revenue"]
        for sale in shop.sales
    )

    # Dictionary comprehension:
    # item name -> total quantity sold
    sales_by_item = {
        name: sum(
            sale["quantity"]
            for sale in shop.sales
            if sale["item"] == name
        )
        for name in shop.items
    }

    # List comprehension for low-stock items
    low_stock_items = [
        item.name
        for item in shop.items.values()
        if item.quantity < low_stock_threshold
    ]

    print(f"Total Revenue: Rs.{total_revenue:.2f}")

    # Find top-selling item
    if shop.sales:

        top_selling_item = max(
            sales_by_item,
            key=sales_by_item.get
        )

        top_quantity = sales_by_item[top_selling_item]

        print(
            f"Top-selling item: {top_selling_item} "
            f"({top_quantity} units)"
        )

    else:
        print("Top-selling item: No sales")

    # Display low-stock items
    if low_stock_items:
        print(
            f"Low-stock items "
            f"(below {low_stock_threshold} units):"
        )

        for item in low_stock_items:
            print(f"  - {item}")

    else:
        print(
            f"Low-stock items "
            f"(below {low_stock_threshold} units): None"
        )

    print("===================================")


def generate_detailed_report(shop):
    """
    Print a more detailed report.
    """

    print("\n========== DETAILED REPORT ==========")

    if not shop.items:
        print("There are no items in the inventory.")
        print("=====================================")
        return

    print(f"Different products: {len(shop.items)}")

    total_units = sum(
        item.quantity
        for item in shop.items.values()
    )

    total_sold = sum(
        item.total_sold
        for item in shop.items.values()
    )

    total_revenue = shop.get_total_revenue()

    print(f"Units currently in stock: {total_units}")
    print(f"Units sold: {total_sold}")
    print(f"Total revenue: Rs.{total_revenue:.2f}")

    print("\nProduct performance:")

    # Dictionary comprehension
    product_report = {
        item.name: {
            "stock": item.quantity,
            "sold": item.total_sold,
            "value": item.quantity * item.price
        }
        for item in shop.items.values()
    }

    for name, data in product_report.items():
        print(
            f"- {name}: "
            f"Stock={data['stock']}, "
            f"Sold={data['sold']}, "
            f"Stock Value=Rs.{data['value']:.2f}"
        )

    print("=====================================")