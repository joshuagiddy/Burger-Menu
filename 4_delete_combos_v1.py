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






combo_name = easygui.enterbox("Enter the combo name to delete:")
if combo_name in combos:
    del combos[combo_name]
    easygui.msgbox(f"Combo {combo_name} deleted successfully!", "Combo Deleted")
else:
    easygui.msgbox("Combo not found!", "Error")

