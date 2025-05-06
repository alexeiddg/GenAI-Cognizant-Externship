def task_1():
    name = 'Alexei'
    age = 20
    height = 5.11

    # Printed w/formatting, cool huh!
    print(f"Hello World (again!) I'm {name}, and I am {age} years old. {height} by the way.")

def task_2():
    """
    Task 2, using operators to do operations on numbers.
    let's make rocket-science level math easy!
    """
    num1 = 4422
    num2 = 5

    # Addition: when two become one... larger!
    print("\nAddition!")
    print(f"Addition of {num1} and {num2} is: {num1 + num2}")

    # Subtraction: num1 politely removes num2 from the equation
    print("\nSubtraction!")
    print(f"Subtraction of {num1} and {num2} is: {num1 - num2}")

    # Multiplication: the magic of turning a little into a lot (less is more I guess)!
    print("\nMultiplication!")
    print(f"Multiplication of {num1} and {num2} is: {num1 * num2}")

    # Division: splitting num1 into equal parts — no actual slicing involved 🍰
    print("\nDivision!")
    print(f"Division of {num1} and {num2} is: {num1 / num2}")

def task_3():
    user_numer = input("\nEnter a number: ")
    user_numer = int(user_numer)

    if user_numer > 0:
        print("This number is positive. Awesome!")
    elif user_numer < 0:
        print("This number is negative. Better luck next time!")
    else:
        print("Zero it is. A perfect balance!")


def main():
    task_1()
    task_2()
    task_3()

if __name__ == '__main__':
    main()