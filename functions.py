# -*- coding: utf-8 -*-
"""functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PaY2yt9DpF59phKO_UyvIImTGF-_I676
"""

import random


def initialize_grid():
    grid = [[0] * 4 for _ in range(4)]  # list comprehension: [0]*4 represent [0,0,0,0]
    for _ in range(2):  # The underscore _ is a convention often used in Python to indicate a variable that is not going to be used within the loop.
        # Since we don't need the loop variable (just the iteration itself), _ is used as a placeholder.
        row = random.randint(0, 3)  # generates random row and column indices within the range [0, 3] (inclusive).
        col = random.randint(0, 3)  # because the grid is 4x4, so the valid indices range from 0 to 3.

        while (
            grid[row][col] != 0
        ):  # This loop continues generating random row and column indices until it finds a position in the grid where the value is 0.
            # ensures that the new random position chosen is an empty cell in the grid.
            col = random.randint(0, 3)
            row = random.randint(0, 3)
        grid[row][col] = 2  # Once an empty cell is found, this line assigns the value 2 to that cell.
    return grid


def print_grid(grid):
    for row in grid:
        print(
            "|", end=""
        )  # | at beginning of each row. The end="" argument ensures that the subsequent prints in the same line instead of moving to the next line.
        for num in row:
            if num == 0:  # if the current number (num) is equal to 0, replaced by a formatted string period (.) with width of 4 characters.
                print("{:>4}".format("."), end="")  # The > aligns the content to the right within the specified width of 4 characters.
            else:
                print("{:>4}".format(num), end="")
        print(" |")  # After printing all the elements in the current row, | at the end of the row, indicating the end of that row.


def generate_new_cell(grid):
    # create a list called empty_cells, iterates over each row i and each column j in the grid (with indices ranging from 0 to 3)
    # checks if the value at that position in the grid is equal to 0 (indicating an empty cell).
    # If it is, it adds the tuple (i, j) representing the coordinates of that empty cell to the list empty_cells.
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]

    if empty_cells:  # empty_cells will contain the coordinates of all the empty cells in the grid, checks if empty_cells is not empty
        row, col = random.choice(
            empty_cells
        )  # selects a random empty cell from empty_cells, assigns the row index to row and the column index to col.
        grid[row][
            col
        ] = 2  # sets the value of the randomly chosen empty cell to 2, which generating a new cell with value 2 in a random empty position of the grid.


# For the following moving functions, use i represent row, j represent column, and k represent comparison


def move_left(grid):
    for i in range(4):  # iterates over each row of the grid.
        for j in range(3):  # iterates over each column of the grid from left to right, except for the last column.
            # because the movement operation is performed by comparing each cell with the cell to its immediate right.
            # Since there is no cell to the right of the last column, there's no need to perform this comparison for the cells in the last column.
            for k in range(
                j + 1, 4
            ):  # The variable k represents the index of the column being compared to the current column j which is the right column
                if grid[i][k] != 0:  # if the right cell is not equal to 0, indicating that there is a non-empty cell to current's right.

                    # if current cell is 0(empty)
                    # moves the right's value (grid[i][k]) into the current cell (grid[i][j])
                    # and sets the cell to the right to 0, effectively moving the non-empty cell to the left.
                    if grid[i][j] == 0:
                        grid[i][j] = grid[i][k]
                        grid[i][k] = 0

                    # If the current cell (grid[i][j]) is not empty and has the same value as the right cell (grid[i][k])
                    # doubles the value of the current cell (grid[i][j]) by multiplying it by 2 and sets the cell to the right to 0,
                    # effectively merging two cells with the same value into one with double the value.
                    elif grid[i][j] == grid[i][k]:
                        grid[i][j] *= 2
                        grid[i][k] = 0
                    break  # the function will move the non-empty cell to the left until it encounters another non-empty cell or reaches the edge of the grid.
                    # ex. if current cell is non-empty but right cell is empty, the next iteration will use last current as right cell because iteration start over


def move_right(grid):
    for i in range(4):  # iterates over each row of the grid
        for j in range(3, 0, -1):  # iterates over each column of the grid from right to left, except for the first column.
            # because the movement operation is performed by comparing each cell with the cell to its immediate left.
            # Since there is no cell to the left of the first column, there's no need to perform this comparison for the cells in the first column.
            # range(3, 0, -1) generates the sequence [3, 2, 1], iterating from the third column to the first column in reverse order.
            for k in range(j - 1, -1, -1):  # generates a sequence starting from j - 1 and ending at -1, iterating in reverse order.
                # This ensures that k iterates over the columns to the left of j, including j - 1, down to the first column (0).
                # sequence for k is [2, 1, 0]
                if grid[i][k] != 0:  # if the left cell is not-empty

                    # if the current cell is 0, move the left value to current cell and set left to be 0
                    if grid[i][j] == 0:
                        grid[i][j] = grid[i][k]
                        grid[i][k] = 0

                    # if the current cell is equal to left cell, double the current value and set left to be 0
                    elif grid[i][j] == grid[i][k]:
                        grid[i][j] *= 2
                        grid[i][k] = 0
                    break


def move_up(grid):
    for j in range(4):  # iterates over each column of the grid.
        for i in range(3):  # iterates over each row of the grid from top to buttom, except for the last row.
            # because the movement operation is performed by comparing each cell with the cell to its immediate below.
            # Since there is no cell to the below of the last row, there's no need to perform this comparison for the cells in the last row.
            for k in range(i + 1, 4):  # range(i + 1, 4) generates the sequence [i + 1, i + 2, i + 3],
                # iterating from the row below the current row (i) up to the last row of the grid.
                if grid[k][j] != 0:  # if the below cell is not-empty

                    # if the current cell is empty, move the below value to current cell and set below to be 0
                    if grid[i][j] == 0:
                        grid[i][j] = grid[k][j]
                        grid[k][j] = 0

                    # if the current cell is equal to below cell, then double the current value and set the below to be 0
                    elif grid[i][j] == grid[k][j]:
                        grid[i][j] *= 2
                        grid[k][j] = 0
                    break


def move_down(grid):
    for j in range(4):  # iterates over each column of the grid.
        for i in range(3, 0, -1):  # iterates over each row of the grid from buttom to top except for the first row.
            # range(3, 0, -1) generates the sequence [3, 2, 1], iterating from the third row to the second row in reverse order.
            for k in range(
                i - 1, -1, -1
            ):  # range(i - 1, -1, -1) generates a sequence starting from i - 1 and ending at -1, iterating in reverse order.
                # This ensures that k iterates over the rows above i, including i - 1, down to the first row (0).
                # sequence for k is [2, 1, 0]
                if grid[k][j] != 0:  # if the above value is not-empty

                    # if the current value is 0, move the above value to current cell and set above to be 0
                    if grid[i][j] == 0:
                        grid[i][j] = grid[k][j]
                        grid[k][j] = 0

                    # if the current value is equal to above cell, then double the current value and set the above to be 0
                    elif grid[i][j] == grid[k][j]:
                        grid[i][j] *= 2
                        grid[k][j] = 0
                    break


def check_win(grid):
    for row in grid:
        for num in row:
            if num == 2048:
                return True
    return False


def check_loss(
    grid,
):  # This function checks if the game is over due to no more valid moves
    for i in range(4):
        for j in range(4):  # iterate over each cell of the grid. i and j represent the row and column indices, respectively.
            if grid[i][j] == 0:  # if the current cell (grid[i][j]) contains a value of 0, indicating an empty cell.
                return False  # if any cell in the grid is empty, the game is not lost, so the function immediately returns False.

            # checks if the current cell (grid[i][j]) is not in the last row (i != 3)
            # and if the value of the current cell is equal to the value of the cell directly below it (grid[i + 1][j]).
            # If any two adjacent cells in the same column have the same value and they are not in the last row, it means the game is not lost
            # ex. even if last two cell in the same column has value of 2, it will merge to 4 with move functions, generate a new 2 wouldn't save the game
            # ex. if the last cell is 2, there is not room to generate a new 2 for further merge
            if i != 3 and grid[i][j] == grid[i + 1][j]:
                return False

            # checks if the current cell (grid[i][j]) is not in the last column (j != 3)
            # and if the value of the current cell is equal to the value of the cell directly to its right (grid[i][j+1])
            if j != 3 and grid[i][j] == grid[i][j + 1]:
                return False
    return True
