import math
import random

MAX_GRID_SIZE = 10
MAX_GUESSES = 4


def get_number(prompt):
    while True:
        player_input = input(prompt)
        try:
            return int(player_input)
        except ValueError:
            print("That's not a valid number! Try again.")


def play_game():
    print("EVIL ALIEN")
    print("==========")

    correct_x_coordinate = random.randint(1, MAX_GRID_SIZE)
    correct_y_coordinate = random.randint(1, MAX_GRID_SIZE)
    correct_distance = random.randint(1, MAX_GRID_SIZE)

    for attempt in range(MAX_GUESSES):

        print(f"(Guess {attempt + 1}/{MAX_GUESSES})")
        x_coordinate = get_number(f"X position (0-{MAX_GRID_SIZE}) > ")
        y_coordinate = get_number(f"Y position (0-{MAX_GRID_SIZE}) > ")
        distance = get_number(f"Distance (0-{MAX_GRID_SIZE}) > ")

        if (
            x_coordinate == correct_x_coordinate
            and y_coordinate == correct_y_coordinate
            and distance == correct_distance
        ):
            print("*BOOM* YOU GOT HIM!")
            break

        direction = ""
        if y_coordinate > correct_y_coordinate:
            direction += "North"
        elif y_coordinate < correct_y_coordinate:
            direction += "South"

        if x_coordinate > correct_x_coordinate:
            direction += "East"
        elif x_coordinate < correct_x_coordinate:
            direction += "West"

        if direction != "":
            print(f"Shot was {direction}")

        if distance > correct_distance:
            print("Too Far")
        elif distance < correct_distance:
            print("Not far enough")

    else:
        print("YOUR TIME HAS RUN OUT!!!")
        print(
            f"(He was at X {correct_x_coordinate}, Y {correct_y_coordinate}, Distance {distance}"
        )


if __name__ == "__main__":
    play_game()
