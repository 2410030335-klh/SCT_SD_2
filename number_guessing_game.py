"""Number guessing game with range hints and attempt tracking."""

import random


def play_game():
    secret = random.randint(1, 100)
    attempts = 0
    print("\nNUMBER GUESSING GAME")
    print("I selected a number from 1 to 100. Can you guess it?")

    while True:
        raw = input("Your guess (or q to quit): ").strip()
        if raw.lower() == "q":
            print(f"Game ended. The number was {secret}.")
            return
        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a whole number between 1 and 100.")
            continue
        if not 1 <= guess <= 100:
            print("Your guess must be between 1 and 100.")
            continue

        attempts += 1
        if guess < secret:
            print("Too low! Try a higher number.")
        elif guess > secret:
            print("Too high! Try a lower number.")
        else:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            return


def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
