import random


def update_game_state(
    secret_word: str,
    guessed_letters: list[str],
    guess: str,
    lives: int) -> tuple[list[str], int, str]:

    if lives <= 0:
        return guessed_letters, 0, "Game over. No more guesses allowed."

    guess = guess.strip().lower()
    secret_word = secret_word.strip().lower()

    guessed_letters = [letter.strip().lower() for letter in guessed_letters]

    required_letters = {c for c in secret_word if c.isalpha()}
    if required_letters <= set(guessed_letters):
        return guessed_letters, lives, "You already guessed the word!"

    if len(guess) != 1 or not guess.isalpha():
        return guessed_letters, lives, "Invalid input. Please enter a single letter."

    if guess in guessed_letters:
        return guessed_letters, lives, "You have already guessed that letter. Try again."

    if guess in secret_word:
        new_guessed_letters = guessed_letters + [guess]
        return new_guessed_letters, lives, "Correct guess!"
    else:
        new_lives = max(lives - 1, 0)
        return guessed_letters, new_lives, "Wrong guess. You lost a life."


def get_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    return " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in secret_word
    )


def is_word_guessed(secret_word: str, guessed_letters: list[str]) -> bool:
    required_letters = {c for c in secret_word if c.isalpha()}
    return required_letters <= set(guessed_letters)



def main():

    word_list = ["apple", "house", "smile", "grape", "chair", "table", "cindy"]

    secret_word = random.choice(word_list)

    guessed_letters = []
    wrong_guesses = []
    lives = 6

    print("Welcome to Hangman!")

    while lives > 0 and not is_word_guessed(secret_word, guessed_letters):

        print("\nWord:", get_masked_word(secret_word, guessed_letters))
        print("Lives:", lives)
        print("Wrong guesses:", " ".join(wrong_guesses))

        guess = input("Guess a letter: ")

        new_letters, new_lives, message = update_game_state(
            secret_word,
            guessed_letters,
            guess,
            lives
        )

        print(message)

        if new_lives < lives:
            wrong_guesses.append(guess.strip().lower())

        guessed_letters = new_letters
        lives = new_lives

    if is_word_guessed(secret_word, guessed_letters):
        print("\nCongratulations! You guessed the word:", secret_word.upper())
    else:
        print("\nYou lost! The word was:", secret_word.upper())


if __name__ == "__main__":
    main()