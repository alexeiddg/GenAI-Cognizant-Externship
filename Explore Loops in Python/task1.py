def main():
    user_number = int(input('Enter the starting number: '))
    while user_number > 0:
        print(user_number)
        user_number -= 1
    if user_number == 0:
        print('Blast off! 🚀', end='')


if __name__ == '__main__':
    main()