import random

print("                         Welcome!!! \n                This is Number Guessing Game")
print("==" * 45)

print(" =====Pick your level===== \n1. Easy \n2. Medium \n3. Hard")
levels = {
    1: ("Easy", 1, 50),
    2: ("Medium", 1, 100),
    3: ("Hard", 1, 500),
}


def get_level():
    while True:
        try:
            level = int(input("Enter level (1-3): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue
        if level in levels:
            return level
        print("Please choose 1, 2, or 3.")


def ask_to_continue():
    while True:
        choice = input("Do you want to play again? [Y/N]: ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            print("Oh, you don't want to play another round.")
            return False
        print("Invalid choice. Enter Y or N.")


def get_guess(start_range, end_range):
    while True:
        try:
            guess = int(input(f"Enter your guess ({start_range}-{end_range}): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        if start_range <= guess <= end_range:
            return guess
        print(f"Please enter a number between {start_range} and {end_range}.")


def play_round(level):
    level_name, start_range, end_range = levels[level]
    number = random.randint(start_range, end_range)
    attempts = 0
    print(f"You chose {level_name}: Range = {start_range} to {end_range}")
    while True:
        attempts += 1
        guess = get_guess(start_range, end_range)
        if guess == number:
            print(f"Congratulations! You guessed it in {attempts} attempt{'s' if attempts != 1 else ''}.")
            break
        if guess < number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")


def main():
    while True:
        lev = get_level()
        play_round(lev)
        if not ask_to_continue():
            break


if __name__ == "__main__":
    main()


        
        

