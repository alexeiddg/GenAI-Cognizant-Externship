import random

def main():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    user_guess = 0

    while attempts < 10:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if user_guess == number_to_guess:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break
        elif user_guess < number_to_guess:
            print(f"{user_guess} Too low! Try again.")
        elif user_guess > number_to_guess:
            print(f"{user_guess} Too high! Try again.")

    if user_guess != number_to_guess:
        print(f"Too many attempts! Game Over. The number was {number_to_guess}.")

if __name__ == '__main__':
    main()
