import sys
from typing import Dict


def ft_inventory_system() -> None:

    args = sys.argv[1:]

    inventory: Dict[str, int] = dict()
    for arg in args:
        if ":" in arg:
            name, qty = arg.split(":", 1)
            try:
                inventory[name] = int(qty)
            except ValueError:
                continue

    if not inventory:
        print(
            "No items in inventory. Please provide items like sword:1 potion:5"
        )
        return

    print("=== Inventory System Analysis ===")

    total_item = sum(inventory.values())
    print(f"Total items in inventory: {total_item}")

    print(f"Unique item type: {len(inventory)}\n")

    print("=== Current Inventory ===")
    for item, qty in sorted(inventory.items(),
                            key=lambda x: x[1], reverse=True):
        percent = qty / total_item * 100
        unit = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit} ({percent:.1f}%)")

    print()
    print("=== Inventory Statistics ===")
    most_abundant = max(inventory.items(), key=lambda x: x[1])[0]
    least_abundant = min(inventory.items(), key=lambda x: x[1])[0]
    most_qty = inventory[most_abundant]
    least_qty = inventory[least_abundant]
    unit_most = "unit" if most_qty == 1 else "units"
    unit_least = "unit" if least_qty == 1 else "units"
    print(
        f"Most abundant: {most_abundant} ({most_qty} {unit_most})"
    )
    print(
        f"Least abundant: {least_abundant} ({least_qty} {unit_least})\n"
    )

    print("=== Item Categories ===")
    moderate = {item: qty for item, qty in inventory.items() if qty >= 5}
    scarce = {item: qty for item, qty in inventory.items() if qty < 5}
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}\n")

    print("=== Management Suggestions ===")
    restock = {item for item, qty in inventory.items() if qty <= 1}
    print(f"Restock needed: {restock}\n")

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    sample_item = "sword"
    print(
        "Sample lookup - "
        f"'{sample_item}' in inventory: {sample_item in inventory}"
    )


if __name__ == "__main__":
    ft_inventory_system()
