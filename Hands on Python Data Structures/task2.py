def main():
    # dictionary to store information about yourself with the following keys: "name", "age", "city".
    my_dict = {
        'name': 'Alexei',
        'age': 20,
        'city': 'Guadalajara'
    }

    # Add a new key-value pair to the dictionary for "favorite color".
    my_dict.update({'favorite color': 'blue'})

    # Update the "city" key with a new value.
    my_dict.update({'city': 'Mexico City'})

    # Print all the keys and values using a loop.
    print('Keys:', ', '.join(my_dict.keys()))
    print('Values:', ', '.join(str(value) for value in my_dict.values()))

if __name__ == '__main__':
    main()