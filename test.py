def find_combo():
    combo_name = easygui.enterbox("Enter the combo name to search:")
    if combo_name in combos:
        details = combos[combo_name]
        item_text = ""
        for item, price in details["items"].items():
            item_text += f"{item}: ${price}\n"
        combo_text = f"{combo_name}:\n{item_text}Total Price: ${details['total_price']}"
        easygui.msgbox(combo_text, "Combo Details")
    else:
        easygui.msgbox("Combo not found!", "Error")
