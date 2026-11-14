# SCT_SD_2 — Number Guessing Game

A command-line game in which the computer selects a random integer from 1 to 100 and the player tries to guess it.

## Features
- Random secret number for every round.
- Hints tell the player whether the guess is too high or too low.
- Counts valid guesses and reports the attempt count on success.
- Handles non-numeric and out-of-range input.
- Supports replay and quitting.

## Run
Requires Python 3.8 or newer. No third-party packages are needed.

```bash
python number_guessing_game.py
```

## How to play
Enter a whole number between 1 and 100. Follow the hints until you find the secret number. Enter `q` to quit the current round.
