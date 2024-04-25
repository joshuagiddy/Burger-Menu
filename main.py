import easygui

# Updated combo menu
combos = {
    "Value": {
        "items": {
            "Beef burger": 2.0,
            "Fries": 1.5,
            "Fizzy drink": 2.19
        },
        "total_price": 5.69
    },
    "Cheezy": {
        "items": {
            "Cheeseburger": 3.0,
            "Fries": 1.5,
            "Fizzy drink": 2.19
        },
        "total_price": 6.69
    },
    "Super": {
        "items": {
            "Cheeseburger": 3.0,
            "Large fries": 2.5,
            "Smoothie": 1.19
        },
        "total_price": 6.69
    }
}

def display_menu():
    menu_text = "Menu:\n\n"
    for combo, details in combos.items():
        item_text = ""
        for item, price in details["items"].items():
            item_text += f"{item}: ${price}\n"
        menu_text += f"{combo}:\n{item_text}Total Price: ${details['total_price']}\n\n"
    easygui.msgbox(menu_text, "Combo Meal Menu")

def add_combo():
    combo_name = easygui.enterbox("Enter the combo name:")
    items = {}
    total_price = 0
    while True:
        item_name = easygui.enterbox("Enter item name (or leave blank to finish adding items):")
        if not item_name:
            break
        item_price = easygui.enterbox("Enter item price:")
        items[item_name] = float(item_price)
        total_price += float(item_price)
    total_price = round(total_price, 2)
    combos[combo_name] = {"items": items, "total_price": total_price}
    easygui.msgbox(f"Combo {combo_name} added successfully!", "Combo Added")


def find_combo():
    combo_name = easygui.enterbox("Enter the combo name to find:")
    if combo_name in combos:
        details = combos[combo_name]
        item_text = ""
        for item, price in details["items"].items():
            item_text += f"{item}: ${price}\n"
        combo_text = f"Combo: {combo_name}\nItems:\n{item_text}Total Price: ${details['total_price']}"
        easygui.msgbox(combo_text, "Combo Details")
    else:
        easygui.msgbox("Combo not found!", "Error")

def delete_combo():
    combo_name = easygui.enterbox("Enter the combo name to delete:")
    if combo_name in combos:
        del combos[combo_name]
        easygui.msgbox(f"Combo {combo_name} deleted successfully!", "Combo Deleted")
    else:
        easygui.msgbox("Combo not found!", "Error")

# Main program loop
while True:
    choices = ["Display Menu", "Add Combo", "Search Combo", "Delete Combo", "Exit"]
    choice = easygui.buttonbox("Select an option", choices=choices)

    if choice == "Display Menu":
        display_menu()
    elif choice == "Add Combo":
        add_combo()
    elif choice == "Search Combo":
        find_combo()
    elif choice == "Delete Combo":
        delete_combo()
    elif choice == "Exit":
        break