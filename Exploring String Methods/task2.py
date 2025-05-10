def main():
    cool_word = " hello, python world! "
    stripped_word = cool_word.strip()
    capitalized_word = stripped_word.capitalize()
    replaced_word = capitalized_word.replace('world', 'universe')
    uppercase_word = replaced_word.upper()

    print(f"Using strip() to remove extra spaces: {stripped_word}")
    print(f"Using capitalize() to capitalize the first letter: {capitalized_word}")
    print(f"Using replace() to replace 'world' with 'universe': {replaced_word}")
    print(f"Using upper() to convert the string to uppercase: {uppercase_word}")


if __name__ == "__main__":
    main()