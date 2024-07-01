secret_word = 'illikkal'
dashes = '-' * len(secret_word)
print('what')

def update_dashes():
    empty = ''
    for i in range(len(secret_word)):
        print('placer')


def get_guess():
    for i in range(10):
        print(dashes)
        guess = input('Guess: ')

        if guess in secret_word:
            print('That letter is in the secret word!')
        elif guess not in secret_word:
            print('That letter is not in the secret word!')

            if guess.isupper():
                print('Your guess must be a lowercase letter!')
            if guess.isdigit():
                print('Your guess cannot be a number!')
            if len(guess) > 1:
                print('Your guess must have exactly one character!')


def main():
    get_guess()


main()
