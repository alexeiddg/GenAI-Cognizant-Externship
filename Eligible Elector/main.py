def main():
    # 🧙 Step 1: Ask the user for their age
    # Convert input from string to integer so we can do numeric comparisons
    age = int(input("How old are you? "))

    # Step 2: Check if the user is old enough to vote
    if age >= 18:
        # 🎉 If the user is 18 or older, they are eligible to vote
        print("Congratulations! You are eligible to vote. Go make a difference!")
    else:
        # ⏳ If not, calculate how many years they have left
        remaining_years = 18 - age
        print(f"Oops! You’re not eligible yet. But hey, only {remaining_years} more years to go!")

if __name__ == "__main__":
    main()