def main():
    user_input = int(input("Enter a number to find its factorial: "))
    factorial = 1
    for i in range(1, user_input + 1):
        factorial *= i

    print(f"The factorial of {user_input} is {factorial}")

if __name__ == '__main__':
    main()