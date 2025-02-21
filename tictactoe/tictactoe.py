# Tic tac toe
# print like this
-1 | -1 | -1
-1 | -1 | -1
-1 | -1 | -1


def main():
    my_grid = create_game()
    print_board(my_grid)
    row, col = get_move(1)
    make_move(my_grid, 1, row, col)
    make_move(my_grid, 0, row, col)

    player = 0
    while True:
        # every turn
        get_move(player)
        row, col = get_move(player)
        make_move(grid, player, row, col)
        if player == 0:
            player = 1
        elif player == 1:
            player = 0
        check = check_winner(grid)
        if check != "No winner":
            break
    # game ended
    print(check)


def create_game():
    # create a empty 3x3 list of list
    grid = [[-1] * 3 for _ in range(3)]
    return grid


def make_move(grid, player, row, col):
    # row/col = 0~2
    # player = 0 (O's) or 1 (X's)

    # down below,
    # ensures that the move is within the bounds of the Tic Tac Toe grid (0-2)
    # and the cell where the player wants to move is empty (because it's -1)
    if 0 <= row < 3 and 0 <= col < 3 and grid[row][col] == -1:
        grid[row][col] = player
        return True
    return False


def print_board(grid):
    # print it nicely like at the top
    for row in grid:
        print(f"{row[0]} | {row[1]} | {row[2]}")
    print()


def check_winner(grid):
    for i in range(3):
        # check rows
        if grid[i][0] == grid[i][1] == grid[i][2] != -1:
            return "Player " + grid[i][0] + "is the winner!"

    # check cols
        if grid[0][i] == grid[1][i] == grid[2][i] != -1:
            return "Player " + grid[0][i] + "is the winner!"

    # check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] != -1:
        return "Player " + grid[0][0] + "is the winner!"
    if grid[0][2] == grid[1][1] == grid[2][0] != -1:
        return "Player " + grid[0][2] + "is the winner!"

    # if no one wins yet (the game is still ongoing)
    if -1 not in grid:
        return "Draw"
    else:
        return "No winner"


def get_move(player):
    row = int(input(f"Player {player}, enter the row (0-2): "))
    col = int(input(f"Player {player}, enter the column (0-2): "))
    return row, col


main()
