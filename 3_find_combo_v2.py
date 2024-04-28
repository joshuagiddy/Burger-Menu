import easygui

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
    items = []
    total_price = 0
    while True:
        item_name = easygui.enterbox("Enter item name (or leave blank to finish adding items):")
        if not item_name:
            break
        item_price = float(easygui.enterbox("Enter item price:"))
        items.append([item_name, item_price])
        total_price += item_price
    total_price = round(total_price, 2)
    new_combo = [combo_name, items, total_price]
    combos[combo_name] = new_combo
    easygui.msgbox(f"Combo {combo_name} added successfully!", "Combo Added")


def find_combo(combo_name):
    combo_name = easygui.enterbox("Enter the combo name:")
    for combo in combos:
        if combo == combo_name:
            details = combos[combo_name]
            item_text = ""
            total = 0
            for item, price in details["items"].items():
                total += price
                item_text += f"{item}: ${price}\n"
            combo_text = f"Combo: {combo_name}\nItems:\n{item_text}\nTotal Price: ${total:.2f}"
            easygui.msgbox(combo_text, "Combo Details")
            return
    easygui.msgbox("Combo not found!", "Error")
        


def main():
    while True:
        choice = easygui.buttonbox("Choose an option, or exit:", choices=["Add Combo", "Find Combo", "Display Menu", "Exit"])
        if choice == "Add Combo":
            add_combo()
        elif choice == "Display Menu":
            display_menu()
        elif choice == "Find Combo":
            combo_name = "ComboName"
            find_combo(combo_name)
        elif choice == "Exit":
            break


main()

