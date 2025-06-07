def main_menu() -> int:
    """Display the main menu and return the user's choice."""
    while True:
        try:
            user_opt = int(input("""\nWhat would you like to do?
    1. Add Expense
    2. View All Expenses
    3. View Summary
    4. Exit
    Choose an option: """))
            # Validate user selection
            if user_opt in [1, 2, 3, 4]:
                return user_opt
            print("Invalid option. Please choose 1-4.")

        except ValueError:
            print("Invalid input. Please enter a number.")

def add_expense(expenses):
    """Add a new expense to the expenses dictionary."""
    try:
        # Get expense details from user
        expense_desc = input("Enter expense description: ")
        if not expense_desc:
            print("Description cannot be empty.")
            return

        category = input("Enter category: ")
        if not category:
            print("Category cannot be empty.")
            return

        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return

        # Create expense tuple and add to dictionary
        expense = (expense_desc, amount)

        if category in expenses:
            expenses[category].append(expense)
        else:
            expenses[category] = [expense]

        print("Expense added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_expenses(data):
    """Display all expenses organized by category."""
    if not data:
        print("No expenses recorded yet.")
        return

    for category, expenses in data.items():
        print(f"Category: {category}")
        for desc, amount in expenses:
            print(f"  - {desc}: ${amount:.2f}")

def view_summary(data):
    """Display a summary of total expenses by category."""
    if not data:
        print("No expenses recorded yet.")
        return

    print("Summary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

def main():
    # Initialize expenses dictionary
    expenses = {}

    print('Welcome to the Personal Finance Tracker!')

    try:
        user_opt = main_menu()

        while user_opt != 4:
            if user_opt == 1:
                add_expense(expenses)
            elif user_opt == 2:
                view_expenses(expenses)
            elif user_opt == 3:
                view_summary(expenses)

            user_opt = main_menu()

        print('\nGoodbye!')

    # Handle manual termination
    except KeyboardInterrupt:
        print("\n\nProgram terminated.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
