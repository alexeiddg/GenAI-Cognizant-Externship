def main():
    fave_fruits = ['apple', 'banana', 'orange', 'tangerine', 'pineapple', 'coconut']
    print(f'Original faves: {fave_fruits}')

    # Append a new fruit to the list
    fave_fruits.append('Kiwi')
    print(f'After adding a fruit: {fave_fruits}')

    # Remove one fruit from the list using the remove() method.
    fave_fruits.remove('apple')
    print(f'After removing fruit: {fave_fruits}')

    # Print the list in reverse order using slicing.
    reversed_faves = fave_fruits[::-1]
    print(f'Reversed List: {reversed_faves}')

if __name__ == '__main__':
    main()