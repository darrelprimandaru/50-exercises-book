#14/50 python 50 exercises: restaurant

MENU = {'tofu': 15, 'steak': 20, 'eggs': 5} #create your own global menu dict

def restaurant():
    total = 0 #to store total

    while True: #infinite loop to keep asking for user input
        order = input("What's your order? ").strip() #store it in order, strip leading and trailing whitespace

        if not order: #if empty, break
            break

        if order in MENU: #if user enters a menu item, add price to total and display msg
            price = MENU[order]
            total += price
            print(f'{order} costs {price}, total is now {total}.')

        else: #if user enters smth not in menu, print this msg
            print(f"We don't have {order} today.")

    print(f'Your total is {total}.') #display total


restaurant()