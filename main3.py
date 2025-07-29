def inventory_list_analyzer():
    print("Welcome to Inventory List Analyzer!\n")

    items = []

    while True:
        name = input("Enter item name: ")
        category = input("Enter category: ")
        quantity = int(input("Enter quantity: "))

        items.append({
            "name": name,
            "category": category.lower(),
            "quantity": quantity
        })

        cont = input("\nDo you want to add more items? (y/n): ").lower()
        if cont != 'y':
            break
        print()

    print("\n========== INVENTORY SUMMARY ==========")

    total_items = len(items)
    print(f"\nTotal Different Items: {total_items}")
    names = [item['name'] for item in items]
    print(f"Explanation: You entered {total_items} different items: {', '.join(names)}.")

    total_quantity = sum(item['quantity'] for item in items)
    quantities_str = " + ".join(str(item['quantity']) for item in items)
    print(f"\nTotal Quantity in Stock: {total_quantity}")
    print(f"Explanation: Sum of all quantities: {quantities_str} = {total_quantity}")

    average_quantity = total_quantity / total_items
    print(f"\nAverage Quantity per Item: {average_quantity:.2f}")
    print(f"Explanation: Average = {total_quantity} total / {total_items} items")

    most_stocked = max(items, key=lambda x: x['quantity'])
    print(f"\nMost Stocked Item: {most_stocked['name']} ({most_stocked['quantity']} units)")
    print(f"Explanation: {most_stocked['name']} has the highest quantity among all items.")

    least_stocked = min(items, key=lambda x: x['quantity'])
    print(f"\nLeast Stocked Item: {least_stocked['name']} ({least_stocked['quantity']} units)")
    print(f"Explanation: {least_stocked['name']} has the lowest quantity.")

    print("\n" + "-"*60)

    categories = sorted(set(item['category'] for item in items))
    print(f"\nUnique Categories in Inventory: {categories}")
    print("Explanation: Categories are taken from user input and converted to lowercase.\nNo duplicates are shown here.")

    print("\n" + "-"*60)

    
    print(" Items Sorted by Quantity (High to Low):\n")
    sorted_items = sorted(items, key=lambda x: x['quantity'], reverse=True)
    for idx, item in enumerate(sorted_items, 1):
        print(f"{idx}. {item['name']} - {item['quantity']} units")
    print("\nExplanation: Items are sorted using the quantity field from highest to lowest.")

    print("\n" + "-"*60)

    print(" Categories in Alphabetical Order:\n")
    for idx, cat in enumerate(categories, 1):
        print(f"{idx}. {cat}")
    print("\nExplanation: The set of unique categories was sorted alphabetically for display.")

    print("\n========== END OF REPORT ==========")


inventory_list_analyzer()