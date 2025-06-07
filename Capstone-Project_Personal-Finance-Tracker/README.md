# Personal Finance Tracker

Welcome to the **Personal Finance Tracker** — a command-line Python application that helps users track their expenses by category. This tool allows you to record expenses, view all recorded expenses, and see a summary of your spending.

---

## 📌 Project Overview

This program simulates a real-world finance tracker. It allows users to:

- Add an expense with a description, category, and amount
- View all recorded expenses grouped by category
- View a summary showing the total amount spent in each category
- Handle invalid inputs gracefully
- Exit the program using a menu-driven interface

Expenses are stored in memory using a Python dictionary, with categories as keys and lists of `(description, amount)` tuples as values.

---

## 🛠️ How to Run the Script

### Requirements
- Python 3.x installed on your system

### Steps
1. **Clone the repository** (or download the `finance_tracker.py` file):
   ```bash
   git clone https://github.com/alexeiddg/python-capstone-finance-tracker.git
   cd python-capstone-finance-tracker  
    ```
   
2. **Run the script**
    ```bash
   python finance_tracker.py
   ```
   
3. Use the menu to interact
Welcome to the Personal Finance Tracker!
```
What would you like to do?
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit
Choose an option:
   ```

## 📚 Python Concepts Used

This project demonstrates the following key Python programming concepts:

- **Functions**: Code is organized into reusable functions for better modularity and readability.
- **Dictionaries**: Used to store and organize expense data by category.
- **Tuples**: Each individual expense is stored as a tuple `(description, amount)`.
- **Loops**: A `while` loop is used to keep the menu running until the user exits.
- **Conditional Statements**: Used for input validation and menu navigation.
- **Exception Handling**: Gracefully handles invalid numeric input, empty strings, and other runtime errors using `try-except` blocks.
- **User Input Validation**: Ensures the program doesn’t crash due to unexpected or invalid input.

## Example Interaction
```
Welcome to the Personal Finance Tracker!

What would you like to do?
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit
Choose an option: 1
Enter expense description: Lunch
Enter category: Food
Enter amount: 12.5
Expense added successfully.

What would you like to do?
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit
Choose an option: 2
Category: Food
  - Lunch: $12.50
```

