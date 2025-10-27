"""Inventory Management System Module.

This module provides functions to add, remove, load, save,
and print inventory data stored in a JSON file.
"""
import json
import logging
from datetime import datetime
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# Global variable
stock_data = {}
def add_item(item="default", qty=0, logs=None):
    """Add a specific quantity of an item to the inventory."""
    if not item:
        return
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.error("Invalid item or quantity type.")
        return
    if qty <= 0:
        logging.warning("Quantity must be positive for item %s", item)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
def remove_item(item, qty):
    """Remove a specific quantity of an item from the inventory."""
    if item not in stock_data:
        logging.warning("Item '%s' not found.", item)
        return
    stock_data[item] -= qty
    if stock_data[item] <= 0:
        del stock_data[item]
    logging.info("Removed %d of %s", qty, item)
def get_qty(item):
    """Get the quantity of an item from the inventory."""
    return stock_data.get(item, 0)
def load_data(file="inventory.json"):
    """Load data from the inventory."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            stock_data.clear()
            stock_data.update(data)
    except (FileNotFoundError, json.JSONDecodeError):
        logging.warning("File not found or corrupt. Starting with empty stock.")
        stock_data.clear()
def save_data(file="inventory.json"):
    """Save Data from the inventory."""
    with open(file, "w", encoding="utf-8") as f:

        json.dump(stock_data, f, indent=4)
def print_data():
    """Print Data from the inventory."""
    print("Items Report:")
    for i in stock_data:
        print(i, "->", stock_data[i])
def check_low_items(threshold=5):
    """Check low items from the inventory."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result
def main():
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()

    load_data()
    print_data()
   

if __name__ == "__main__":
    main()

