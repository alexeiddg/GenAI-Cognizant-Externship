"""Reusable Main Menu, returns the option the user selects as int"""
def main_menu() -> int:
    user_opt = int(input(""" \nPlease choose an option:
    1. View inventory
    2. Add an item
    3. Remove an item
    4. Update an item
    5. Calculate total value
    6. Exit
    > """))

    return user_opt

def main(user_opt):
    # Default dict inventory items
    inventory = {
        'apple': (10, 2.5),
        'banana': (20, 1.2),
    }

    # While loop runs the program until the user wants to exit with user_opt = 6
    while user_opt != 6:
        # List every item of the dict
        if user_opt == 1:
            print('\nCurrent inventory:')
            for key, value in inventory.items():
                # Since each value is a tuple (quantity, price), we access its elements by index
                print(f'Item: {key}, Quantity: {value[0]}, Price: {value[1]}\n', end='')
        # Add Item
        elif user_opt == 2:
            print('\nAdd an Item: ')
            # Collect all data to add a new item
            item_name = str(input("Enter the item's name: ").strip())
            item_quantity = int(input('Enter the item\'s quantity: '))
            item_value = float(input('Enter the item\'s value: '))
            # Try to add the item, if it fails print the error so it won't break the program
            try:
                inventory.update({item_name: (item_quantity, item_value)})
                print('Inventory Updated!')
            except ValueError as e:
                print(e)
        # Remove an item
        elif user_opt == 3:
            print('\nRemove an Item: ')
            # Get the key of the item to remove
            target_item = str(input('Enter the item\'s name: '))
            # try to remove item, if it fails print the error so it won't break the program
            try:
                inventory.pop(target_item)
                print('Item Removed!')
            except KeyError as e:
                print(e)
        # Update item
        elif user_opt == 4:
            print('\nUpdate an Item: ')
            # get target key
            target_item = str(input('Enter the item\'s name: '))
            update_opt = int(input('What would you like to update?\n1. Item Quantity \n2. Item Value\n> '))

            if update_opt == 1:
                item_quantity = int(input('Enter the item\'s quantity: ')) # get the new value
                _, current_value = inventory[target_item] # get current values
                # replace the value (a tuple) for an existing key with a new tuple
                inventory[target_item] = (item_quantity, current_value)
            if update_opt == 2:
                item_value = float(input('Enter the item\'s value: '))
                current_quantity, _ = inventory[target_item]
                inventory[target_item] = (current_quantity, item_value)

        # Calculate total value
        elif user_opt == 5:
            total_value = 0
            # unpack tuple into (quantity, price) and multiply price * quantity to find the total value
            for item, (quantity, price) in inventory.items():
                total_value += price * quantity

            print(f'\nTotal value: {total_value:.2f}')
        # break the loop
        elif user_opt == 6:
            break
        # if user_opt returns an invalid number, break the loop
        else:
            print('Option not recognized')
            break

        user_opt = main_menu()

    print('\nGoodbye! 👋🏻')

if __name__ == '__main__':
    print('Welcome to the Inventory Manager!')
    main(user_opt=main_menu())