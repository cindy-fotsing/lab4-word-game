from main import update_game_state


def test_correct_guess_appends_letter_and_keeps_lives() -> None:
    guessed, lives, message = update_game_state("apple", ["a", "p"], "l", 5)

    assert guessed == ["a", "p", "l"]
    assert lives == 5
    assert message == "Correct guess!"


def test_wrong_guess_decrements_lives_without_appending() -> None:
    guessed, lives, message = update_game_state("apple", ["a", "p"], "z", 5)

    assert guessed == ["a", "p"]
    assert lives == 4
    assert message == "Wrong guess. You lost a life."


def test_invalid_guess_returns_normalized_letters_and_same_lives() -> None:
    guessed, lives, message = update_game_state("apple", [" A ", "P"], "12", 5)

    assert guessed == ["a", "p"]
    assert lives == 5
    assert message == "Invalid input. Please enter a single letter."


def test_repeated_guess_is_case_insensitive() -> None:
    guessed, lives, message = update_game_state("apple", ["A", "p"], "a", 5)

    assert guessed == ["a", "p"]
    assert lives == 5
    assert message == "You have already guessed that letter. Try again."


def test_game_over_when_lives_is_zero_blocks_updates() -> None:
    guessed, lives, message = update_game_state("apple", [" A "], "a", 0)

    assert guessed == [" A "]
    assert lives == 0
    assert message == "Game over. No more guesses allowed."


def test_already_won_blocks_any_new_guess() -> None:
    guessed, lives, message = update_game_state("apple", ["a", "p", "l", "e"], "z", 5)

    assert guessed == ["a", "p", "l", "e"]
    assert lives == 5
    assert message == "You already guessed the word!"


def test_strips_secret_word_and_guess_before_matching() -> None:
    guessed, lives, message = update_game_state(" apple ", ["a", "p"], " l ", 5)

    assert guessed == ["a", "p", "l"]
    assert lives == 5
    assert message == "Correct guess!"


def test_non_alphabetic_chars_in_secret_word_do_not_block_won_state() -> None:
    guessed, lives, message = update_game_state("don't", ["d", "o", "n", "t"], "x", 5)

    assert guessed == ["d", "o", "n", "t"]
    assert lives == 5
    assert message == "You already guessed the word!"


def test_lives_never_go_negative() -> None:
    guessed, lives, message = update_game_state("apple", ["a"], "z", 1)

    assert guessed == ["a"]
    assert lives == 0
    assert message == "Wrong guess. You lost a life."
