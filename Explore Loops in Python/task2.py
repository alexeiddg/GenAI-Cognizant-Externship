def main():
    user_number = int(input("Enter a number to see its multiplication table: "))
    for i in range(1, 11):
        print(f"{user_number} x {i} = {user_number * i}")

if __name__ == '__main__':
    main()
