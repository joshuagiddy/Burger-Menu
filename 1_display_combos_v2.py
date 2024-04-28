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





user_input = easygui.buttonbox("Select an option", choices=["Display Menu", "Exit"])

def display_menu():
    menu_text = "Menu:\n\n"
    for combo, details in combos.items():
        item_text = ""
        for item, price in details["items"].items():
            item_text += f"{item}: ${price}\n"
        menu_text += f"{combo}:\n{item_text}Total Price: ${details['total_price']}\n\n"
    easygui.msgbox(menu_text, "Combo Meal Menu")

if user_input == "Display Menu":
   display_menu()
elif user_input == "Exit":
    easygui.msgbox("Exiting program.")
else:
    easygui.msgbox("Invalid input.", "Error")
