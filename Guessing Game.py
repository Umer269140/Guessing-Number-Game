
import random

def guessing_game():
    """
    A simple number guessing game where the user guesses a number between 1 and 100.
    """
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    guessing_game()
    
