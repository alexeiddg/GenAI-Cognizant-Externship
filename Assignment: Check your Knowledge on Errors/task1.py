def main():
    # Loop to allow retries
    while True:
        try:
            user_opt = int(input("Enter a number: "))
            result = 100 / user_opt
        # Handle division by Zero
        except ZeroDivisionError:
            print("You can't divide by zero!")
        # Handle invalid or non-integer input
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        # If no errors, return the result
        else:
            print(f'100 Divided by {user_opt} is: {result:.1f}')
            break

if __name__ == '__main__':
    main()