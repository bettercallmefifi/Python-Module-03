import sys


def ft_inventory_system():

    args = sys.argv[1:]

    inventory = dict()
    for arg in args:
        if ":" in arg:
            name, qty = arg.split(":")
            inventory[name] = int(qty)

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
    for item, qty in sorted(inventory.items(), key=lambda x: -x[1]):
        parcent = qty / total_item * 100
        unit = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit} ({parcent:.1f}%)")

    print()
    print("=== Inventory Statistics ===")
    most_abundant = max(inventory.items(), key=lambda x: x[1])[0]
    least_abundant = min(inventory.items(), key=lambda x: x[1])[0]
    unit = "unit" if most_abundant == 1 else "units"
    print(
        f"Most abundant: {most_abundant} ({inventory[most_abundant]} {unit})"
    )
    unitos = "unit" if qty == 1 else "units"
    print(
        f"Least abundant: {least_abundant}"
        f"({inventory[least_abundant]} {unitos})\n"
    )

    print("=== Item Categories ===")
    moderate = {
        item: qty for item, qty in inventory.items() if qty >= 5
    }
    scarce = {item: qty for item, qty in inventory.items() if qty < 5}
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}\n")

    print("=== Management Suggestions ===")
    restock = {item for item, qty in inventory.items() if qty <= 1}
    print(f"Restock needed: {restock}\n")

    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary value: {list(inventory.values())}")
    sample_item = "sword"
    print(
        "Sample lookup - "
        f"'{sample_item}' in inventory: {sample_item in inventory}"
    )


if __name__ == "__main__":
    ft_inventory_system()
