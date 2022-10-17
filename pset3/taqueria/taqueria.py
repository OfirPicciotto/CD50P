import decimal

def main():
    place_order()


def place_order():
    sum = 0
    menu = {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
            }
    while True:
        try:
            menu_item = input("Choose an item: ").title()
            if menu_item in menu:
                sum += round(decimal.Decimal(menu[menu_item]),2)
                print(f"Total: ${round(decimal.Decimal(sum),2)}")
        except EOFError:
            print()
            break

main()