import turtle

# Reusable main menu, returns selection option
def main_menu() -> int:
    # Loop for validation, keep asking for a valid int
    while True:
        try:
            # Bad indent needed so it displays correctly on the console
            user_opt = int(input(
    """Welcome to the Recursive Artistry Program!
    Choose an option:
    1. Calculate Factorial 
    2. Find Fibonacci 
    3. Draw a Recursive Fractal 
    4. Exit
    > """))

            # Check input is a valid option
            if user_opt in (1, 2, 3, 4):
                return user_opt
        # Try again if input is not a valid option
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Calculate factorial
def calculate_factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    # Recursively call function
    return n * calculate_factorial(n - 1)

# Calculate fibonacci
def calculate_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursively call function
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

def recursive_fractal(branch_length: int = 100, angle: int = 20):

    def draw_branch(t, length, ang):
        if length > 5:
            # Draw the current branch
            t.forward(length)

            # Draw the right sub-branch
            t.right(ang)
            draw_branch(t, length - 15, ang)

            # Return to original heading and draw the left sub-branch
            t.left(ang * 2)
            draw_branch(t, length - 15, ang)

            # Restore orientation and position
            t.right(ang)
            t.backward(length)

    # Set up turtle screen and turtle
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Setup turtle object and config
    t = turtle.Turtle()
    t.color("green")
    t.left(90)
    t.speed("fastest")

    # Begin drawing from the root
    draw_branch(t, branch_length, angle)

    screen.mainloop()

def main():
    user_opt = main_menu()

    # Main app loop
    while user_opt != 4:
        if user_opt == 1:
            # try loop so that the app does not crash w/incorrect input
            try:
                factorial = int(input('\nEnter a number to find its factorial: '))
                # Validate input is a positive number
                if factorial < 0:
                    print("Please enter a non-negative integer.\n")
                else:
                    print(f'The factorial of {factorial} is {calculate_factorial(factorial)}\n')
            except ValueError:
                print("Invalid input! Please enter an integer.\n")
        elif user_opt == 2:
            try:
                pos = int(input('\nEnter the position of the Fibonacci number: '))
                # Validate input
                if pos < 0:
                    print("Please enter a non-negative integer.\n")
                else:
                    print(f'The {pos}th Fibonacci number is {calculate_fibonacci(pos)}\n')
            except ValueError:
                print("Invalid input! Please enter an integer.\n")
        elif user_opt == 3:
            print("\nDrawing fractal tree!\n")
            recursive_fractal()

        user_opt = main_menu()

    print('Thank you for using Recursive Artistry!')

if __name__ == '__main__':
    main()