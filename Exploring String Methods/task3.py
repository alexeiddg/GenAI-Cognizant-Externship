def main():
    word_input = input("Enter a word: ").lower().strip().replace(" ", "")
    reversed_word = word_input[::-1]

    if reversed_word == word_input:
        print(f'Yes, {word_input} is a palindrome!')
    else:
        print(f'No, {word_input} is not a palindrome.')

if __name__ == "__main__":
    main()