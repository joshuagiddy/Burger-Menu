import easygui

combos = [
    ["Value",
     [
         ["Beef burger", 2.0],
         ["Fries", 1.5],
         ["Fizzy drink", 2.19]
     ],
     5.69
     ],
    ["Cheezy",
     [
         ["Cheeseburger", 3.0],
         ["Fries", 1.5],
         ["Fizzy drink", 2.19]
     ],
     6.69
     ],
    ["Super",
     [
         ["Cheeseburger", 3.0],
         ["Large fries", 2.5],
         ["Smoothie", 1.19]
     ],
     6.69
     ]
]


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
    combos.append(new_combo)
    easygui.msgbox(f"Combo {combo_name} added successfully!", "Combo Added")


add_combo()
