"""Add_combos_v1
We are now adding a part of the program which will add whatever combo the user wants"""
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


combo_name = easygui.enterbox("Enter the combo name:")
items = {}
total_price = 0
while True:
    item_name = easygui.enterbox("Enter item name (or leave blank to finish adding items):")
    if not item_name:
        break
    item_price = easygui.enterbox("Enter item price:")
easygui.msgbox(f"Combo {combo_name} added successfully!", "Combo Added")



