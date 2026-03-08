import math
import random

MAX_HEIGHT = 100
MAX_GUESSES = 8


def get_number(prompt):
    while True:
        player_input = input(prompt)
        try:
            return int(player_input)
        except ValueError:
            print("That's not a valid number! Try again.")


def play_game():
    print("INTERGALATIC GAMES")
    print("==================")

    height = random.randint(1, MAX_HEIGHT)
    print(f"You must launch a satellite to a height of {height}")

    correct_radians = math.atan(height / 3)
    correct_angle = int(math.degrees(correct_radians))

    correct_velocity = int(3000 * math.sqrt(height + 1 / height))

    for attempt in range(MAX_GUESSES):

        print(f"(Guess {attempt + 1}/{MAX_GUESSES})")
        angle = get_number(f"Enter angle (0-90) > ")
        velocity = get_number(f"Enter speed (0-40000) > ")

        if abs(angle - correct_angle) < 2 and abs(velocity - correct_velocity) < 100:
            print("YOU'VE DONE IT")
            print("NCTV WINS-THANKS TO YOU")
            break

        if angle - correct_angle < -2:
            print("Too shallow", end=" ")
        elif angle - correct_angle > 2:
            print("Too steep", end=" ")

        if velocity - correct_velocity < -100:
            print("Too slow")
        elif velocity - correct_velocity > 100:
            print("Too fast")

    else:
        print("YOU'VE FAILED")
        print("YOU'RE FIRED")
        print(f"(The required angle was {correct_angle} and speed {correct_velocity}")


if __name__ == "__main__":
    play_game()
