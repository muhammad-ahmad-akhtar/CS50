import inflect

order = inflect.engine()
namesList = []

while True:
    try:
        name = input("Name: ").strip().title()
        namesList.append(name)
    except EOFError or name == 'A':
        print(f"Adieu, adieu, to {order.join(namesList)}")
        break