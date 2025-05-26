def main():
    # try block to attempt division and collect input
    try:
        number_1 = int(input('Enter the first number: '))
        number_2 = int(input('Enter the second number: '))
        result = number_1 / number_2
    # Handle invalid or non-integer input
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    # Handle Zero division
    except ZeroDivisionError:
        print("You can't divide by zero!")
    # If no errors raised, print the result
    else:
        print(f'The result is: {result:.1f}')
    # Run the closing statement always
    finally:
        print('Thank you for using this program!')

if __name__ == '__main__':
    main()