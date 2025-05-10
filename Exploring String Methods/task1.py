def main():
    normal_word = 'Python is amazing!'

    # Get first 6 chars using slicing
    python_word = normal_word[0:6]

    # Extract 'amazing' using slicing
    amazing_word = normal_word[10:17]

    # Reverse word
    reversed_word = normal_word[::-1]

    print(f"First word: {python_word}")
    print(f"Amazing part: {amazing_word}")
    print(f"Reversed part: {reversed_word}")


if __name__ == '__main__':
    main()