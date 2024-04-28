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


user_input = easygui.buttonbox("Select an option?", choices=["Display Menu", "Exit"])

if user_input == "Display Menu":
   easygui.msgbox(combos)
elif user_input == "No":
    easygui.msgbox("Exiting program.")
else:
    easygui.msgbox("Invalid input.", "Error")
user_input
