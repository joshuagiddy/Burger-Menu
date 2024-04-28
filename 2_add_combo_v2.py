"""Add_combo_v2
Now we are creating it into a function so that we can use it for the main program as well as display combos
The function will allow it to calculate the price of the items and the total price of the combo and store the information."""
import easygui
def add_combo():
    combo_name = easygui.enterbox("Enter the combo name:")
    items = []
    total_price = 0
    while True:
        item_name = easygui.enterbox("Enter item name (or leave blank to finish adding items):")
        if not item_name:
            break
        item_price = float(easygui.enterbox("Enter item price (without dollar sign): "))
        items.append([item_name, item_price])
        total_price += item_price
    total_price = round(total_price, 2)
    new_combo = [combo_name, items, total_price]
    combos.append(new_combo)
    easygui.msgbox(f"Combo {combo_name} added successfully!", "Combo Added")




