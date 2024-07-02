def update_word(secret_word, dashes, guess):
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            result += guess
        else:
            result += dashes[i]
    return result


def display_game_state(dashes, incorrect_guesses):
    print(f"Current word: {dashes}")
    print(f"Incorrect guesses: {incorrect_guesses}")
    print(f"Remaining attempts: {10 - len(incorrect_guesses)}")


def main():
    secret_word = 'illikkal'
    dashes = '-' * len(secret_word)
    incorrect_guesses = []
    correct_guesses = set()

    while True:
        display_game_state(dashes, incorrect_guesses)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in correct_guesses or guess in incorrect_guesses:
            print("You already guessed that letter.")
            continue

        if guess in secret_word:
            correct_guesses.add(guess)
            dashes = update_word(secret_word, dashes, guess)
        else:
            incorrect_guesses.append(guess)

        if dashes == secret_word:
            print(f"Congratulations! You've guessed the word: {secret_word}")
            break

        if len(incorrect_guesses) >= 10:
            print(f"Sorry, you've lost! The word was: {secret_word}")
            break


main()
