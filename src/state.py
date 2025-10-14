class GameState:
    def __init__(self, board_size=4):
        self.board_size = board_size
        self.board = self.initialize_board()
        self.score = 0
        self.game_over = False

    def initialize_board(self):
        board = [[0] * self.board_size for _ in range(self.board_size)]
        self.add_random_tile(board)
        self.add_random_tile(board)
        return board

    def add_random_tile(self, board):
        import random
        empty_tiles = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if board[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            board[i][j] = random.choice([2, 4])

    def save_state(self):
        return {
            'board': self.board,
            'score': self.score,
            'game_over': self.game_over
        }

    def load_state(self, state):
        self.board = state['board']
        self.score = state['score']
        self.game_over = state['game_over']