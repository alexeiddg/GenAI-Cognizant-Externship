def main():
    user_password = input("Enter your password: ")

    # Length: It should be at least 8 characters.
    # Contain at least one uppercase letter, one lowercase letter, one digit, and one special character (like @, #, $).

    # List of tuples to evaluate password and display corresponding message
    # tuple items (condition, error message, points)
    checks = [
        # Check length
        (len(user_password) >= 8, "Password must be at least 8 characters long.", 2),
        # Check if any char in password is uppercase
        (any(c.isupper() for c in user_password), "Password must contain at least one uppercase letter.", 2),
        # Check if any char in password is lowercase
        (any(c.islower() for c in user_password), "Password must contain at least one lowercase letter.", 2),
        # Check if any char in password is a number
        (any(c.isdigit() for c in user_password), "Password must contain at least one digit.", 2),
        # check if any char is '@#$' in password
        (any(c in '@#$' for c in user_password), "Password must contain at least one special character (@, #, or $).", 2)
    ]

    score = 0
    failed_messages = []

    for condition, message, points in checks:
        if condition:
            # Sum points for each condition met
            score += points
        else:
            # Collect error messages for the criteria that is not met
            failed_messages.append(message)

    # print each error message
    if failed_messages:
        for msg in failed_messages:
            print(f"- {msg}")
    # valid password
    else:
        print("Your password is strong! 💪")

    if score == 10:
        print("Strength: Excellent 💪")
    elif score >= 8:
        print("Strength: Strong ✅")
    elif score >= 6:
        print("Strength: Fair ⚠️")
    else:
        print("Strength: Weak ❌")

    print(f"\n🔒 Password Strength Score: {score}/10")

if __name__ == "__main__":
    main()