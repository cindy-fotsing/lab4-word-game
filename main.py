"""Hangman game logic for processing player guesses and updating game state."""


def update_game_state(
    secret_word: str,
    guessed_letters: list[str],
    guess: str,
    lives: int) -> tuple[list[str], int, str]:
    """
    Process a single guess and return updated state.

    Normalizes all inputs to lowercase and strips whitespace.
    Filters secret_word to only alphabetic characters for win-condition checks.
    Returns original guessed_letters on invalid input; appends new letter only on correct guess.

    Args:
        secret_word: Word to guess (case-insensitive, whitespace-tolerant).
        guessed_letters: List of previously guessed letters (normalized during call).
        guess: Player's input (stripped and lowercased).
        lives: Remaining guesses (clamped to 0 minimum).

    Returns:
        tuple of (updated_guessed_letters, updated_lives, message).
        guessed_letters is only updated on a correct, new guess.
        lives decrements only on wrong, new guess.
    """

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