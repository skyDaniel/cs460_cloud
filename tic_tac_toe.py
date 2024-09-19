import ipywidgets as widgets
from IPython.display import display, clear_output

# Initialize the game state
board = [' ' for _ in range(9)]
current_player = 'X'
game_over = False

# Game logic functions
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2],  # Rows
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # Columns
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # Diagonals
        [2, 4, 6],
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_tie(board):
    return all(space != ' ' for space in board)

def disable_all_buttons():
    for button in buttons:
        button.disabled = True

def make_move(b, position):
    global current_player, game_over
    if not game_over and board[position] == ' ':
        board[position] = current_player
        b.description = current_player
        b.disabled = True
        if check_winner(board, current_player):
            status.value = f"🎉 Player {current_player} wins!"
            game_over = True
            disable_all_buttons()
        elif check_tie(board):
            status.value = "It's a tie!"
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            status.value = f"Player {current_player}'s turn"

# Create game buttons
buttons = [widgets.Button(description=' ', layout=widgets.Layout(width='60px', height='60px')) for _ in range(9)]
for i, button in enumerate(buttons):
    button.on_click(lambda b, i=i: make_move(b, i))

# Create status label
status = widgets.Label(value=f"Player {current_player}'s turn")

# Arrange buttons in a grid
grid = widgets.GridBox(children=buttons, layout=widgets.Layout(
    width='200px',
    grid_template_columns='60px 60px 60px',
    grid_template_rows='60px 60px 60px',
    grid_gap='5px'
))

# Display the game
display(status)
display(grid)

# Reset function
def reset_game(b):
    global board, current_player, game_over
    board = [' ' for _ in range(9)]
    current_player = 'X'
    game_over = False
    status.value = f"Player {current_player}'s turn"
    for button in buttons:
        button.description = ' '
        button.disabled = False

# Create and display reset button
reset_button = widgets.Button(description='Reset Game', button_style='info')
reset_button.on_click(reset_game)
display(reset_button)

