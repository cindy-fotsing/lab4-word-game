# My Original Thinking

## App states
- For a game like Hangman, we first have to start game, then guest the correct letters of the word and for each wrong letter, we get a strike that brings us closer to losing.

## App Variables
- For the variables, we have secret_word, lives_remaining, letters_left

## App Rules and Invariants
- Lives cannot be negative

## App Bugs
-Entering numbers instead of letters

# CoPilot Suggestions

## App states
For a simple Hangman-style game, the minimum useful states are:
Start or Idle: the game has not begun yet.
Playing: the player is actively guessing letters.
Won: the whole word has been revealed.
Lost: the player has no lives left.
A useful distinction for your notes in MY_NOTES.md is that invalid input, like typing a number, is usually not a separate state. It is usually just an event handled while the game is in Playing. The game stays in Playing, shows an error, and asks again.
So if you want the cleanest answer, your App states section could say:
Start
Playing
Won
Lost

## App Variables
For a Hangman-style game, the main idea is to keep only the variables that represent the current truth of the game. In your notes in MY_NOTES.md, secret_word and lives_remaining are good starts, but letters_left is often better treated as a derived value instead of stored separately.
A clean minimal set would be:
secret_word: the word the player is trying to guess.
guessed_letters: all letters the player has already entered.
lives_remaining: how many wrong guesses are still allowed.
game_state: whether the game is start, playing, won, or lost.
Two other variables are often useful depending on how you structure the program:
wrong_letters: only the incorrect guesses, if you want to show them separately.
max_lives: the starting number of lives, if you do not want to hardcode it everywhere.
What you usually do not need to store separately:
letters_left: you can compute it from secret_word and guessed_letters.
The displayed word like _ a _ g _ a n: this can also be computed when needed.
So the strongest answer for your notes is probably:
secret_word
guessed_letters
lives_remaining
game_state

## App Rules and Invariants
For Hangman, use this distinction:
Rules: how the game changes after an input.
Invariants: what must always stay true.
Rules
On start: pick secret_word, set lives_remaining = max_lives, clear guessed_letters, set game_state = playing.
A guess must be exactly one letter (normalize to lowercase).
If the guess is new and in secret_word, reveal all matching positions.
If the guess is new and not in secret_word, decrement lives_remaining by 1.
If the guess was already made, apply one consistent policy (ignore it, or penalize it).
game_state = won when all distinct letters in secret_word are guessed.
game_state = lost when lives_remaining == 0 before winning.
If game_state is won or lost, guesses no longer modify the round.
Invariants
0 <= lives_remaining <= max_lives
secret_word is non-empty and unchanged during a round.
guessed_letters contains unique letters only.
game_state is always one of start, playing, won, lost.
If game_state == won, every distinct letter of secret_word is in guessed_letters.
If game_state == lost, then lives_remaining == 0.
Displayed mask (like _ a _ _) always has the same length as secret_word.

## App Bugs
Great section to think about early. Common Hangman bugs are usually in input handling, state transitions, and win/loss checks.
Invalid input accepted: empty string, numbers, symbols, or more than one character treated as a real guess.
Case mismatch: A and a treated differently, causing correct letters to be marked wrong.
Repeated guess bug: guessing the same letter twice incorrectly removes another life (or is counted twice in history).
Lives underflow: lives_remaining goes below 0.
Off-by-one lives: player loses one guess too early or too late.
Wrong win condition: checking guessed positions instead of unique letters, so words with repeated letters behave incorrectly.
Incomplete reveal: only first occurrence of a letter is shown instead of all occurrences.
Game continues after end: guesses still modify data after won or lost.
State not reset on restart: old guessed_letters or old lives_remaining leaks into new round.
Inconsistent tracking: guessed_letters, wrong_letters, and displayed mask get out of sync.
Word normalization bug: secret word includes spaces/hyphens/uppercase but guess logic assumes only lowercase a-z.
Hidden crash paths: pressing Enter, EOF input, or unexpected whitespace causes exceptions.
Infinite/stuck loop: loop condition never exits after won/lost.
Display mismatch: shown mask length differs from the secret word length.
Random-word edge case: empty string or invalid word from word list causes broken round setup.