# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oShuEGJt9n_Kglto8qUqaIwmGuIDkMGZ
"""

from functions import *
import os


def main():
    grid = (
        initialize_grid()
    )  # initializes the game grid using the initialize_grid() function, creating a 4x4 grid with two randomly placed tiles of value 2.
    print("Welcome to 2048!")
    print_grid(grid)

    while (
        True
    ):  # initiates an infinite loop, ensuring that the game continues until the player either wins or loses and the loop is explicitly broken.
        print("Use WASD keys to move the tiles (W: up, A: left, S: down, D: right)")  # prompts the user to enter a move using the WASD keys,
        move = input("Enter your move: ").upper()  # converts the input to uppercase, and stores it in the variable move.
        # os.system('cls' if os.name == 'nt' else 'clear')
        # This line clears the console screen to provide a cleaner output after each move.
        # It checks the operating system and uses the appropriate command (cls for Windows, clear for Unix-based systems).

        try:  # Depending on the user's input, the appropriate movement function is called, modifying the grid accordingly.
            if move == "W":
                move_up(grid)
            elif move == "A":
                move_left(grid)
            elif move == "S":
                move_down(grid)
            elif move == "D":
                move_right(grid)
            else:  # # The raise statement is used to raise a ValueError exception, If the user enters an invalid move (ie., other than "W", "A", "S", or "D")
                raise ValueError("Invalid move! Use WASD keys.")  # a ValueError is raised, and an error message is printed.

        # This block handles exceptions that occur within the try block.
        # If a ValueError exception is raised within the try block, the code inside the except block is executed.
        except ValueError as e:  # The except block catches the ValueError exception and assigns it to the variable e.
            print(e)  # the error message (e) is printed to inform the user that their input was invalid.
            continue  # continue statement is used to skip the rest of the current iteration of the loop and move to the next iteration.
            # allows the program to prompt the user for input again after an invalid move

        generate_new_cell(
            grid
        )  # After each valid move, a new tile with a value of 2 is generated on an empty cell using the generate_new_cell(grid) function.
        print_grid(grid)

        if check_win(grid):  # After each move, the check_win(grid) function is called to check if the player has won.
            print("Congratulations! You've won!")
            break
        elif check_loss(grid):
            print("Game over! You've lost.")
            break


if __name__ == "__main__":
    main()
