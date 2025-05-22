def make_sandwich(*args):
    print('Making a sandwich with the following ingredients:')
    for arg in args:
        print(f'- {arg} ')

def main():
    make_sandwich('bacon', 'lettuce', 'tomato',)

if __name__ == '__main__':
    main()