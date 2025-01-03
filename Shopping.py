items = ['Bread', 'Cookies', 'Butter', 'Cheese', 'Yoghurt']
prices = [40, 80, 120, 180, 60]
cart = []

while True:
    print('\nEnter 1 for viewing the items')
    print('Enter 2 for adding the items in cart')
    print('Enter 3 for updating the items in cart')
    print('Enter 4 for deleting the items in cart')
    print('Enter 5 for printing bill')
    print('Enter 6 to exit')
    choice = int(input('Enter the choice: '))

    if choice == 1:
        for i in range(len(items)):
            print(f'Name: {items[i]} Price: {prices[i]}')

    elif choice == 2:
        item_name = input('Enter the item name: ') 
        quantity = int(input('Enter the quantity: ')) 
        if item_name in items: 
            for i in range(len(items)): 
                if items[i] == item_name: 
                    cart.append([item_name, quantity, price[i]])

    elif choice == 3:
        item_name = input('Which item to be updated: ')
        quantity = int(input('Enter the quantity to be updated: '))
        for item in cart:
            if item[0] == item_name:
                item[1] = quantity

    elif choice == 4:
        item_name = input('Which item to be removed: ') 
        for item in cart: 
            if item[0] == item_name:
                cart.remove(item)

    elif choice == 5:
        total_amount = 0 
        bill_list = [] 
        for item in cart: name, quantity, price = item 
        total = price * quantity 
        total_amount += total 
        bill_list.extend([name, quantity, price, total]) 
        print(f'Bill List: {bill_list}')

    elif choice == 6:
        print("Name,Quantity,Price,Total") 
        total_amount = 0 
        for item in cart: 
            name, quantity, price = item 
            total = price * quantity 
            total_amount += total 
            print([name, quantity, price, total]) 
        print(f'Total Amount of Bill {total_amount}')
        break

    else:
        print('Invalid choice! Please try again.')
