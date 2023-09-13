
# set up a 5 x 5 board
board = ["."] * 5

# initialize and print board
for i in range(5):
   board[i] = ["0"] * 5
print(board)

# populate board with . for possible letters and None for blank squares (row and column are both odd numbers)
for x in range(5):
    for y in range(5):
        if x % 2 != 0 and y % 2 !=0:
            board[y][x] = None
        else:
            board[y][x] = "."
print(board)

# There are always 6 5-letter words.

# Intersecting_letters at (0,0), (0,2), (0,4), (2,0), (2,2), (2,4), (4,0), (4,2), (4,4).

# Board must contain 9 intersecting letters--an intersecting letter is
# where one distinct word intersects with exactly one other distinct word.

# Each of the 6 5-letter words intersects with exactly 3 other words.

# A letter is an intersecting letter if the row and the column are not both odd, and 
# if the row number = the column number + 0, 1, or 2 multiples of 2.

# Solver gets 15 swaps to solve the puzzle, so puzzle must be solvable in 15.

# There is an unproven claim that all puzzles are solvable in 10. This will be an interesting
# claim to test programmatically.

# Key is the same as in Wordle: . (black) = absent, lower-case = present (yellow),
# upper-case (green) = certain.