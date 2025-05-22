def describe_pet(pet_name: str, animal_type='dog'):
    print(f'I have a {animal_type} named {pet_name}.')

def main():
    describe_pet('Chrysler')
    describe_pet('Whiskers', 'cat')

if __name__ == '__main__':
    main()