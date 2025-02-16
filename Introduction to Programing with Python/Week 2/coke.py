print("Amount Due: 50")
amount_due = 50
while(True):
    user_input = int(input("Insert Coin: "))
    if user_input == 25:
        amount_due -= 25
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        else:
            print(f"Change Owed: {amount_due*-1}")
            break
    elif user_input == 10:
        amount_due -= 10
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        else:
            print(f"Change Owed: {amount_due*-1}")
            break
    elif user_input == 5:
        amount_due -= 5
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        else:
            print(f"Change Owed: {amount_due*-1}")
            break
    else:
        print(f"Amount Due: {amount_due}")