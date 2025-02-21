import pygame

# pygame setup
pygame.init()
font = pygame.font.Font(None, 36)
SCREEN_WIDTH = 500  # 500 pixels wide
SCREEN_HEIGHT = 500
GRID_SIZE = 5  # 5X5 BOARD

CELL_SIZE = SCREEN_WIDTH // GRID_SIZE  # how big is each square -> 100
NUM_SHIPS = 5
NUM_GUESSES = 8

# ship_img = pygame.image.load("")
# hit_img = pygame.image.load("")
# miss_img = pygame.image.load("")

# ship_img = pygame.transform.scale(ship_img, (CELL_SIZE, CELL_SIZE))
# hit_img = pygame.transform.scale(hit_img, (CELL_SIZE, CELL_SIZE))
# miss_img = pygame.transform.scale(miss_img, (CELL_SIZE, CELL_SIZE))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battleship Game")
clock = pygame.time.Clock()
running = True

board = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
]


def draw_grid():
    """Draw the grid with row x col squares."""
    # Fill the background with white first
    screen.fill("white")
    if placing_ships:
        instruction_text = "Place your ships!"
    elif guessing_ships:
        instruction_text = "Guess where the ships are!"
    elif game_result:
        instruction_text = "You won!"
    else:
        instruction_text = "You lost..."
    text_surface = font.render(instruction_text, True, "black")
    screen.blit(text_surface, (10, 10))
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            # Draw squares with a border and no fill
            square = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, "black", square, width=5)


def draw_board(hide_ships):
    # double for loop same as draw_grid
    # for each elemetn in the 2D board:
    # if we see "x" and hide_ships == False: draw a ship on that spot
    # color it blue for your own
    # if we see "o": guess (hit)
    # color it green if you hit it
    # if we see ".": guess (missed)
    # color it red if you missed it
    # circle(surface, color, center, radius, width=0, draw_top_right=None, draw_top_left=None, draw_bottom_left=None, draw_bottom_right=None)
    # row = 0 -> y = 50 -> (row * CELL_SIZE) + CELL_SIZE / 2
    # col = 0 -> x = 50 -> (col * CELL_SIZE) + CELL_SIZE / 2
    # row = 1 -> y = 150 -> (row * CELL_SIZE) + CELL_SIZE / 2
    # row = 2 -> y = 250 -> (row * CELL_SIZE) + CELL_SIZE / 2

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = (col * CELL_SIZE) + CELL_SIZE / 2
            y = (row * CELL_SIZE) + CELL_SIZE / 2
            if board[row][col] == "x" and hide_ships == False:
                pygame.draw.circle(screen, "blue", (x, y), CELL_SIZE / 2)
            elif board[row][col] == "o":
                pygame.draw.circle(screen, "green", (x, y), CELL_SIZE / 2)
            elif board[row][col] == ".":
                pygame.draw.circle(screen, "red", (x, y), CELL_SIZE / 2)


def place_battleship(row, col):
    if board[row][col] == " ":
        board[row][col] = "x"
        return True
    return False


def place_guess(row, col):
    if board[row][col] == "o" or board[row][col] == ".":
        raise ValueError(f"You already guessed this spot {row}{col}!")
    # returns True if we hit a boat, return False if we missed
    if board[row][col] == "x":
        board[row][col] = "o"
        return True
    else:  # missed guess
        board[row][col] = "."
        return False


def convert_click_to_grid(x, y):
    """Convert mouse click position (x, y) to (row, col) on grid."""
    # YOUR TURN
    # ans = (0,0)
    # x = [0,100) => col = 0
    # y = [0,100) => row = 0
    # ans = (0,1)
    # x = [100,200) => col = 1
    # y = [0,100] = row = 0
    # x = [200,300) => col = 2

    col = x // CELL_SIZE
    row = y // CELL_SIZE
    return row, col


# Main game loop
game_result = None
placing_ships = True
guessing_ships = False
num_ships_placed = 0
num_ships_guessed = 0
correct_guesses = 0
while running:
    # poll for events
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # get the mouse position
            x, y = event.pos
            print(f"Screen clicked at {x}, {y}")
            row, col = convert_click_to_grid(x, y)
            print(f"Grid clicked at {row}, {col}")

            if placing_ships:
                # Place Ship Stage
                # call your place ships function
                # +1 to num_ships_placed
                # num_ships_placed == NUM_SHIPS, set placing_ships = False and guessing_ships = True
                if place_battleship(row, col) == False:
                    print("Invalid spot! Try again.")
                else:  # valid placement
                    num_ships_placed += 1
                    print(f"Ship placed! {num_ships_placed}/{NUM_SHIPS} ships placed.")
                if num_ships_placed == NUM_SHIPS:
                    placing_ships = False
                    guessing_ships = True
            elif guessing_ships:
                print("Guess")
                try:
                    hit = place_guess(row, col)
                    num_ships_guessed += 1
                    if hit:
                        print("Hit!")
                        correct_guesses += 1
                    else:
                        print("Miss!")
                    if correct_guesses == NUM_SHIPS:
                        print("You win!")
                        guessing_ships = False
                        game_result = True
                    elif num_ships_guessed == NUM_GUESSES:
                        guessing_ships = False
                        print("You lost...")
                        game_result = False
                except ValueError as e:
                    print(e)
                # Place Guesses Stage

    draw_grid()
    draw_board(hide_ships=guessing_ships)
    pygame.display.flip()  # updates the screen with new content
    clock.tick(60)  # limits FPS to 60

pygame.quit()

# TODO list:
# Change the circles to png files
# https://www.geeksforgeeks.org/how-to-rotate-and-scale-images-using-pygame/?ref=next_article
# You might one to have different images to represent the ships vs good guesses vs bad guesses (you can load multiple images into the game)
# If you find the white background boring you can also change it to a background image (i.e. a picture of water)
