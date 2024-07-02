import random


def update_dashes(secret_word, dashes, guess):
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            result += guess
        else:
            result += dashes[i]
    return result


def get_guess():
    word_list = ["python", "java", "swift", "javascript", "kotlin"]
    secret_word = random.choice(word_list)
    dashes = '-' * len(secret_word)
    guesses_left = 10

    while True:
        print(dashes)
        print(f"{guesses_left} incorrect guesses left.")
        guess = input('Guess: ')

        if guess in secret_word:
            print('That letter is in the secret word!')
            dashes = update_dashes(secret_word, dashes, guess)
        elif guess not in secret_word:
            print('That letter is not in the secret word!')
            guesses_left -= 1

            if guess.isupper():
                print('Your guess must be a lowercase letter!')
            if guess.isdigit():
                print('Your guess cannot be a number!')
            if len(guess) > 1:
                print('Your guess must have exactly one character!')

        if dashes == secret_word:
            print(f"Congratulations! You've guessed the word: {secret_word}")
            break

        if guesses_left == 0:
            print(f"You lose! The word was: {secret_word}")
            break


def main():
    get_guess()


main()
