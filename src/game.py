# ...existing code...
import random
from copy import deepcopy

class Game:
    def __init__(self, board_size=4):
        self.board_size = board_size
        self.board = None
        self.score = 0
        self.game_over = False
        self.won = False
        # initialize immediately so GUI can read board right after Game() constructed
        self.reset()

    def start_game(self):
        # kept for compatibility, but reset() is the public initializer used by the GUI
        self.board = self.initialize_board()
        self.add_random_tile()
        self.add_random_tile()

    def initialize_board(self):
        return [[0] * self.board_size for _ in range(self.board_size)]

    def add_random_tile(self):
        empty_tiles = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.board[i][j] = random.choice([2, 4])

    # --- core move helpers (functional-style, return new board/score delta) ---
    def _compress_row_left(self, row):
        new_row = [v for v in row if v != 0]
        new_row += [0] * (self.board_size - len(new_row))
        return new_row

    def _merge_row_left(self, row):
        score_gain = 0
        row = row[:]
        for i in range(self.board_size - 1):
            if row[i] != 0 and row[i] == row[i + 1]:
                row[i] *= 2
                row[i + 1] = 0
                score_gain += row[i]
        return row, score_gain

    def _move_left(self, board):
        new_board = []
        total_gain = 0
        for row in board:
            compressed = self._compress_row_left(row)
            merged, gain = self._merge_row_left(compressed)
            final = self._compress_row_left(merged)
            new_board.append(final)
            total_gain += gain
        return new_board, total_gain

    def _transpose(self, board):
        return [list(row) for row in zip(*board)]

    def _reverse_rows(self, board):
        return [list(reversed(row)) for row in board]

    # Public move API - accepts direction strings: "Up", "Down", "Left", "Right"
    def move(self, direction):
        if self.game_over:
            return

        direction = direction.capitalize()
        moved = False
        score_gain = 0
        old = deepcopy(self.board)

        if direction == "Left":
            new_board, score_gain = self._move_left(self.board)
        elif direction == "Right":
            rev = self._reverse_rows(self.board)
            moved_board, score_gain = self._move_left(rev)
            new_board = self._reverse_rows(moved_board)
        elif direction == "Up":
            trans = self._transpose(self.board)
            moved_board, score_gain = self._move_left(trans)
            new_board = self._transpose(moved_board)
        elif direction == "Down":
            trans = self._transpose(self.board)
            rev = self._reverse_rows(trans)
            moved_board, score_gain = self._move_left(rev)
            new_board = self._transpose(self._reverse_rows(moved_board))
        else:
            return  # unknown direction

        if new_board != old:
            moved = True

        if moved:
            self.board = new_board
            self.score += score_gain
            # after a successful move, add a random tile and update status
            self.add_random_tile()
            self.check_win()
            if self.is_game_over():
                self.game_over = True

    def check_win(self):
        for row in self.board:
            if 2048 in row:
                self.won = True
                # mark game_over if you want to stop further moves when winning:
                self.game_over = True
                break

    def _can_move(self):
        # If any empty cell, can move
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == 0:
                    return True
        # Check for any possible merge horizontally or vertically
        for i in range(self.board_size):
            for j in range(self.board_size - 1):
                if self.board[i][j] == self.board[i][j + 1]:
                    return True
        for j in range(self.board_size):
            for i in range(self.board_size - 1):
                if self.board[i][j] == self.board[i + 1][j]:
                    return True
        return False

    def check_loss(self):
        if not self._can_move():
            self.game_over = True
            return True
        return False

    def is_game_over(self):
        # true when no moves available or when already marked game_over/won
        if self.won:
            return True
        if not self._can_move():
            return True
        return False

    # public reset used by GUI/controller
    def reset(self):
        self.score = 0
        self.game_over = False
        self.won = False
        self.board = self.initialize_board()
        self.add_random_tile()
        self.add_random_tile()
        return self.board

    # legacy compatibility
    def reset_game(self):
        return self.reset()
# ...existing code...