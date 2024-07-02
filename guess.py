def update_dashes(secret_word, dashes, guess):
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            result += guess
        else:
            result += dashes[i]
    return result


def main():
    secret_word = 'illikkal'
    dashes = '-' * len(secret_word)
    guesses_left = 0

    while True:
        print(dashes)
        guess = input('Guess: ')

        if guess in secret_word:
            print('That letter is in the secret word!')
            dashes = update_dashes(secret_word, dashes, guess)
            guesses_left += 1
        elif guess not in secret_word:
            print('That letter is not in the secret word!')
            guesses_left += 1

            if guess.isupper():
                print('Your guess must be a lowercase letter!')
            if guess.isdigit():
                print('Your guess cannot be a number!')
            if len(guess) > 1:
                print('Your guess must have exactly one character!')

        if dashes == secret_word:
            print(f"Congratulations! You've guessed the word: {secret_word}")
            break

        if guesses >= 10:
            print(f"Sorry, you've lost! The word was: {secret_word}")
            break


main()
