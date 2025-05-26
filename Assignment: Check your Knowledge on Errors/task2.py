def main():
    # Handle index error
    try:
        my_list = [1, 2, 3]
        print(my_list[5]) # Out of range index: list only has indices 0 to 2
    except IndexError:
        print("IndexError occurred! List index out of range.")

    # Handle Key error
    try:
        my_dict = {'a': 1, 'b': 2, 'c': 3}
        print(my_dict['city']) # key 'city' does not exist
    except KeyError:
        print("KeyError occurred! Key not found in the dictionary.")

    # Handle type error
    try:
        print(result = '25' + 25) # Cannot add string and integer directly
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")

if __name__ == '__main__':
    main()