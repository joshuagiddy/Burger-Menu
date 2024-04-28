"""Add_combo_v3
This is adding it to the display menu function which as you will see, will store whatever combo
is added in the display function"""
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
def display_menu():
    menu_text = "Menu:\n\n"
    for combo, details in combos.items():
        item_text = ""
        for item, price in details["items"].items():
            item_text += f"{item}: ${price}\n"
        menu_text += f"{combo}:\n{item_text}Total Price: ${details['total_price']}\n\n"
    easygui.msgbox(menu_text, "Combo Meal Menu")
# Main Program
while True:
    user_input = easygui.buttonbox("Select an option", choices=["Display Menu", "Add Combo", "Exit"])
    if user_input == "Display Menu":
        display_menu()
    elif user_input == "Add Combo":
        add_combo()
    elif user_input == "Exit":
        easygui.msgbox("Exiting program.")
        exit()
    else:
        easygui.msgbox("Invalid input.", "Error")

