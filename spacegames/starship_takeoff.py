import random

MAX_GUESSES = 10
MAX_GRAVITY = 20
MAX_WEIGHT = 40


def get_number(prompt):
    while True:
        player_input = input(prompt)
        try:
            return int(player_input)
        except ValueError:
            print("That's not a valid number! Try again.")


def play_game():
    print("STARSHIP TAKE-OFF")
    print("=================")

    gravity = random.randint(1, MAX_GRAVITY)
    weight = random.randint(1, MAX_WEIGHT)
    target_force = gravity * weight

    print(f"Gravity = {gravity}")
    print(f"Calculate the required force!")

    for attempt in range(MAX_GUESSES):
        guess = get_number(f"Type in the force (Guess {attempt + 1}/{MAX_GUESSES}) > ")

        if guess > target_force:
            print("Too High")
        elif guess < target_force:
            print("Too Low")
        else:
            print("GOOD TAKE OFF!")
            break

    else:
        print("YOU FAILED - THE ALIENS GOT YOU!")
        print(f"(The required force was {target_force})")


if __name__ == "__main__":
    play_game()
