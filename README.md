# Hangman Word Game

A command-line Hangman implementation in Python.

## Requirements

- Python 3.10+
- pytest (for running tests)

## Setup

Create and activate a virtual environment, then install pytest:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pytest
```

> If activation is blocked by execution policy, run this first:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

## Running the game

```powershell
python main.py
```

## Running the tests

From the project root with the virtual environment activated:

```powershell
python -m pytest -v
```

To run quietly (pass/fail summary only):

```powershell
python -m pytest -q
```

## Project structure

```
main.py          # Game logic (update_game_state)
tests/
  test_main.py   # pytest test suite for update_game_state
```
