def main():
    # Create a tuple with three elements: your favorite movie, song, and book.
    my_tuple = ('Interstellar', 'Run Your Mouth', 'The Midnight Library')
    print(f'Favorite things: {my_tuple}')

    # Trying to change one of the elements
    try:
        my_tuple[2] =  'The Hobbit' # This will raise a TypeError
    except TypeError as e:
        print("Error:", e)

    # Print the length of the tuple using the len() function.
    print(f'Length of my_tuple: {len(my_tuple)}')

if __name__ == '__main__':
    main()