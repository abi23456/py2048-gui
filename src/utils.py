import random

def generate_random_tile():
    """Generate a random tile value (2 or 4)."""
    return random.choice([2, 4])

def get_empty_positions(board):
    """Return a list of empty positions on the board."""
    return [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 0]

def add_random_tile(board):
    """Add a random tile (2 or 4) to a random empty position on the board."""
    empty_positions = get_empty_positions(board)
    if empty_positions:
        i, j = random.choice(empty_positions)
        board[i][j] = generate_random_tile()

def reset_board(size):
    """Create a new game board of the given size with two random tiles."""
    board = [[0] * size for _ in range(size)]
    add_random_tile(board)
    add_random_tile(board)
    return board