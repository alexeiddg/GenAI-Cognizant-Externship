import logging

# logging config
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

# Reusable main menu, returns int
def main_menu() -> int:
    try:
        user_opt = int(input("""Choose an operation: 
    1. Addition 
    2. Subtraction 
    3. Multiplication 
    4. Division 
    5. Exit 
    > """))
    # Validate input
    except ValueError:
        print("\nInvalid input! Please enter a valid number.")
        return main_menu()
    # Validate selected option exists
    if user_opt not in (1, 2, 3, 4, 5, ):
        print("\nInvalid input! Please enter a valid number.")
        return main_menu()
    else:
        return user_opt # return option as int

# function to validate num input is a number
def validate_input(operation: str):
    try:
        number_1 = float(input(f"\nEnter the first number to {operation}: "))
        number_2 = float(input(f"Enter the second number to {operation}: "))
    # catch error for non valid inputs
    except ValueError as e:
        print("\nInvalid input! Please enter a valid number.")
        # log error to file
        logging.error(f'ValueError occurred when validating input: {e}')
        return validate_input(operation)
    # returns both numbers
    else:
        return number_1, number_2

def main():
    print('Welcome to the Error-Free Calculator!')
    user_opt = main_menu()

    while user_opt != 5:
        # sum
        if user_opt == 1:
            num1, num2 = validate_input('Add') # validate input
            try:
                result = num1 + num2
            # catch invalid input that may be uncaught by validate_input()
            except TypeError as e:
                print("\nInvalid input! Please enter a valid number.")
                logging.error(f'TypeError occurred when adding 2 numbers: {e}') # log error to file
            else:
                print(f'The result of {num1} + {num2} = {result:.1f}\n')

        elif user_opt == 2:
            num1, num2 = validate_input('Subtract')
            try:
                result = num1 - num2
            except TypeError as e:
                print("\nInvalid input! Please enter a valid number.")
                logging.error(f'TypeError occurred when subtracting 2 numbers: {e}')
            else:
                print(f'The result of {num1} - {num2} = {result:.1f}\n')

        elif user_opt == 3:
            num1, num2 = validate_input('Multiply')
            try:
                result = num1 * num2
            except TypeError as e:
                print("\nInvalid input! Please enter a valid number.")
                logging.error(f'TypeError occurred when multiplying 2 numbers: {e}')
            else:
                print(f'The result of {num1} * {num2} = {result:.1f}\n')

        elif user_opt == 4:
            num1, num2 = validate_input('Divide')
            try:
                result = num1 / num2
            except TypeError as e:
                print("\nInvalid input! Please enter a valid number.")
                logging.error(f'TypeError occurred when dividing 2 numbers: {e}')
            # For the division catch zero division error
            except ZeroDivisionError as e:
                print("You can't divide by zero!")
                logging.error(f"ZeroDivisionError occurred: {e}")
            else:
                print(f'The result of {num1} / {num2} = {result:.1f}\n')

        user_opt = main_menu()

    print('\nThank you for using the Error-Free Calculator!')

if __name__ == '__main__':
    main()