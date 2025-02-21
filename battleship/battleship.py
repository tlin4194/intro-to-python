"""Battleship (Simplified) Start with empty grid of 5x5.

Each battleship is only 1 cell.
Rows are labelled 1-5, columns are labelled A-E
Round 1: Player 1 places 5 ships by inputting row + col. i.e. "A1" is the top left square.
"""

board = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
]
# row_label = "1" -> row = 0


def convert_row(row_label):
    return int(row_label) - 1


# col_label = "A" -> col = 0
# col_label = "D" -> col = 3


def convert_col(col_label):
    return ord(col_label) - ord("A")


def place_battleship(row_label, col_label):
    # convert labels into row and col index first
    row = convert_row(row_label)
    col = convert_col(col_label)
    # then place the battleship
    if board[row][col] != "x":
        board[row][col] = "x"


def player_guess(row_label, col_label):
    # convert labels into row and col index first
    row = convert_row(row_label)
    col = convert_col(col_label)
    if board[row][col] == "o" or board[row][col] == ".":
        raise ValueError("you already guessed this!")
    # returns True if we hit a boat, return False if we missed
    if board[row][col] == "x":
        board[row][col] = "o"
        return True
    else:
        board[row][col] = "."
        return False


def print_board():
    print("\n  A B C D E")
    print(" +---------+")
    row = 1
    for line in board:
        row_content = ""
        for box in line:
            boxspace = box + " "
            row_content += boxspace
        print(f"{row}|{row_content}|")
        row += 1
    print(" +---------+")


def main():
    print("Start game")
    num_ships = 5
    # player 1 creates a board
    for n in range(num_ships):
        print("Where do you want ship", n + 1, "?")
        col_label = input("column (A to E): ")
        row_label = input("row (1 to 5): ")
        place_battleship(row_label, col_label)
    print_board()
    print("Player 2 has 8 guesses")
    guesses = 8
    hits = 0
    # player 2 start guessing
    for n in range(guesses):
        print("Guess", n + 1, "?")
        col_label = input("column (A to E): ")
        row_label = input("row (1 to 5): ")
        hit_or_miss = player_guess(row_label, col_label)
        if hit_or_miss == True:
            hits += 1
        # if we already hit all the ships, player 2 wins
        if hits == num_ships:
            print("Player 2 won! :)")
            break

    # if we finish guessing and there's < 5 hits, player 2 lost
    print("Player 2 lost... :(")


main()
