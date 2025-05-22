def factorial(number: int):
    if number == 1 or number == 0:
        return 1

    result = number * factorial(number - 1)
    return result


def fibonacci(number: int):
    if number == 0:
        return 0
    elif number == 1:
        return 1

    result = fibonacci(number - 1) + fibonacci(number - 2)
    return result

def main():
    factorial_number = 5
    fibonacci_number = 6
    print(f'Factorial of {factorial_number} is {factorial(factorial_number)}')
    print(f'The {fibonacci_number}th Fibonacci number is {fibonacci(fibonacci_number)}.')

if __name__ == '__main__':
    main()